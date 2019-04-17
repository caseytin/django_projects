# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from autos.models import Auto, Comment
from django.views import View
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from autos.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
from autos.forms import CreateForm, CommentForm

class AutoListView(OwnerListView):
    model = Auto
    template_name = "auto_list.html"

class AutoDetailView(OwnerDetailView):
    model = Auto
    template_name = "auto_detail.html"
    def get(self, request, pk) :
        auto = Auto.objects.get(id=pk)
        comments = Comment.objects.filter(auto=auto).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'auto' : auto, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

class AutoDeleteView(OwnerDeleteView):
    model = Auto
    template_name = "auto_delete.html"

# def stream_file(request, pk) :
#     auto = get_object_or_404(Auto, id=pk)
#     response = HttpResponse()
#     response['Content-Type'] = auto.content_type
#     response['Content-Length'] = len(auto.picture)
#     response.write(auto.picture)
#     return response

# Another way to do it.
# This will handle create and update with an optional pk parameter on get and post
# We don't use the Generic or OwnerGeneric because (a) we need a form with a file
# and (b) we need to to populate the model with request.FILES
class AutoFormView(LoginRequiredMixin, View):
    template = 'auto_form.html'
    success_url = reverse_lazy('autos')
    def get(self, request, pk=None) :
        if not pk :
            form = CreateForm()
        else:
            auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
            form = CreateForm(instance=auto)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=auto)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model ads before saving
        auto = form.save(commit=False)
        auto.owner = self.request.user
        auto.save()
        return redirect(self.success_url)


class CommentCreateView(LoginRequiredMixin, View):
    template = 'auto_form.html'
    success_url = reverse_lazy('autos')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        f = get_object_or_404(Auto, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, auto=f)
        comment.save()
        return redirect(reverse_lazy('auto_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "auto_comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        auto = self.object.auto
        return reverse_lazy('auto_detail', args=[auto.id])
#
# class AutoListView(OwnerListView):
#     model = Auto
#     template_name = "auto_list.html"

    # def get(self, request) :
    #     auto_list = Auto.objects.all()
    #     favorites = list()
    #     if request.user.is_authenticated:
    #         # rows = [{'id': 2}]  (A list of rows)
    #         rows = request.user.favorite_autos.values('id')
    #         favorites = [ row['id'] for row in rows ]
    #     ctx = {'auto_list' : auto_list, 'favorites': favorites}
    #     return render(request, self.template_name, ctx)

# # https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.db.utils import IntegrityError
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AddFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, pk) :
#         print("Add PK",pk)
#         t = get_object_or_404(Auto, id=pk)
#         fav = Fav(user=request.user, auto=t)
#         try:
#             fav.save()  # In case of duplicate key
#         except IntegrityError as e:
#             pass
#         return HttpResponse()
#
# @method_decorator(csrf_exempt, name='dispatch')
# class DeleteFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, pk) :
#         print("Delete PK",pk)
#         t = get_object_or_404(Auto, id=pk)
#         try:
#             fav = Fav.objects.get(user=request.user, auto=t).delete()
#         except Fav.DoesNotExist as e:
#             pass
#
#         return HttpResponse()
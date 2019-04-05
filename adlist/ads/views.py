from django.shortcuts import render

# Create your views here.
from ads.models import Ad
from django.views import View, generic
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from ads.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.forms import CreateForm

class AdListView(OwnerListView):
    model = Ad
    template_name = "ad_list.html"

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "ad_detail.html"

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']
    template_name = "ad_form.html"

    success_url = reverse_lazy('ad')
    def get(self, request, pk=None) :
        form = CreateForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Add owner to the model before saving
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']
    template_name = "ad_form.html"

    success_url = reverse_lazy('ad')
    def get(self, request, pk) :
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        ad.save()
        return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = "ad_delete.html"

class AdFormView(LoginRequiredMixin, View):
    template = 'ad_form.html'
    success_url = reverse_lazy('ad')
    def get(self, request, pk=None) :
        if not pk :
            form = CreateForm()
        else:
            ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
            form = CreateForm(instance=ad)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model owner before saving
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)

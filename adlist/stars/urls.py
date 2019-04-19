from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.StarListView.as_view()),
    path('stars', views.StarListView.as_view(), name='stars'),
    path('star/<int:pk>', views.StarDetailView.as_view(), name='star_detail'),
    path('star/create', views.StarFormView.as_view(success_url=reverse_lazy('stars')), name='star_create'),
    path('star/<int:pk>/update', views.StarFormView.as_view(success_url=reverse_lazy('stars')), name='star_update'),
    path('star/<int:pk>/delete', views.StarDeleteView.as_view(success_url=reverse_lazy('stars')), name='star_delete'),
    path('star/<int:pk>/comment', views.CommentCreateView.as_view(), name='star_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(success_url=reverse_lazy('stars')), name='star_comment_delete'),
    # path('star/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='star_favorite'),
    # path('star/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='star_unfavorite'),
]
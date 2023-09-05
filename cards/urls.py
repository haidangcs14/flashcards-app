from django.urls import path
from . import views

# from django.views.generic import TemplateView

urlpatterns = [
    path(
        "", 
        views.CardListView.as_view(),
        name = "card-list",    
    ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name = "card-create"
    ),
    path(
        "edit/<int:pk>",
        views.UpdateView.as_view(),
        name = "card-update"
    ),
]

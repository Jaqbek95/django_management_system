from django.urls import path

from .views import ProjectsListView, ProjectDetailsView, CustomersListView


urlpatterns = [
    path('projects/', ProjectsListView.as_view()),
    path('projects/<int:id>', ProjectDetailsView.as_view()),
    path('customers/', CustomersListView.as_view()),
]
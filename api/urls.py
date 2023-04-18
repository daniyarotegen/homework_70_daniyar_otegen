from django.urls import path

from api.views import IssueListView, ProjectListView, ProjectDetailView, IssueDetailView

urlpatterns = [
    path('issues/', IssueListView.as_view(), name='issues'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

]
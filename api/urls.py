from django.urls import path
from api.views.issues import IssueListView, IssueDetailView
from api.views.projects import ProjectListView, ProjectDetailView


urlpatterns = [
    path('issues/', IssueListView.as_view(), name='issues'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue_detail_api'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail_api'),

]
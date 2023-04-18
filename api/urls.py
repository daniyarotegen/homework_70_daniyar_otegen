from django.urls import path

from api.views import IssueView

urlpatterns = [
    path('issues/', IssueView.as_view(), name='issues'),

]
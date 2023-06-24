from django.urls import path
from portfolio_app.views import ProjectListView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
]

from django.urls import path
from portfolio_app.views import ProjectListView, IndexView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

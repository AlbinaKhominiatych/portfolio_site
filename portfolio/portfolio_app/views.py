from django.views.generic import TemplateView, ListView
from portfolio_app.models import Project

class IndexView(TemplateView):
    template_name = 'index.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'



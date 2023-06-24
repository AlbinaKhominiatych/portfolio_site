from django.views.generic import ListView
from portfolio_app.models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

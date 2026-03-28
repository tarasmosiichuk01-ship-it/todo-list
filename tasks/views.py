from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")

class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")

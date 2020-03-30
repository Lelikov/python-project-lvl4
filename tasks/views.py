from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from tasks.forms import TaskForm, StatusCreateForm, TagCreateForm
from tasks.models import Tag, Task, TaskStatus, User


class TasksViews(LoginRequiredMixin, ListView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TaskCreate'] = TaskForm
        context['StatusCreateForm'] = StatusCreateForm
        context['TagCreateForm'] = TagCreateForm
        context['TaskStatuses'] = TaskStatus.objects.all()
        context['Users'] = User.objects.all()
        return context

    def get_queryset(self):
        if self.request.GET:
            filters = {}
            params = self.request.GET
            all_fields = [field.name for field in Task._meta.fields]
            for key, value in params.items():
                if value and (key.split('__')[0] in all_fields):
                    filters.update({key: value})
            queryset = super().get_queryset().filter(**filters)
        else:
            queryset = super().get_queryset()
        return queryset


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('TaskViews')
    template_name = 'tasks/task_create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('TaskViews')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator


class TaskEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_edit.html'
    success_url = reverse_lazy('TaskViews')

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.creator


class StatusCreate(LoginRequiredMixin, CreateView):
    model = TaskStatus
    form_class = StatusCreateForm
    success_url = reverse_lazy('TaskViews')
    template_name = 'status/task_status_create.html'


class StatusViews(LoginRequiredMixin, ListView):
    model = TaskStatus
    template_name = 'status/task_status_list.html'


class StatusEdit(LoginRequiredMixin, UpdateView):
    model = TaskStatus
    fields = ('name',)
    template_name = 'status/task_status_edit.html'
    success_url = reverse_lazy('StatusViews')


class StatusDelete(LoginRequiredMixin, DeleteView):
    model = TaskStatus
    success_url = reverse_lazy('StatusViews')


class TagCreate(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ('name',)
    template_name = 'tags/tag_create.html'
    success_url = reverse_lazy('TaskViews')


class TagViews(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tags/tag_list.html'


class TagEdit(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ('name',)
    template_name = 'tags/tag_edit.html'
    success_url = reverse_lazy('TagViews')


class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('TagViews')

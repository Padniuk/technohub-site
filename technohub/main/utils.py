from django.views.generic import FormView, ListView
from main.forms import PostApplicationForm, PostWorkerForm
from main.models import Service
from django.contrib import messages

class HomeMixin(ListView, FormView):

    form_class = PostApplicationForm
    model = Service
    context_object_name = 'services'
    service_type = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        filtered_services = self.get_queryset()
        for service in filtered_services:
            service.individual_services = [s.strip() for s in service.services.split(',')]
        context['services'] = filtered_services
        return context
    
    def get_queryset(self):
        return self.model.objects.filter(service_type=self.service_type)

    def form_valid(self, form):
        application = form.save(commit=False)
        application.application_type = self.service_type
        application.save()

        messages.success(self.request, 'Форму успішно відправлено!')
        return super().form_valid(form)


class WorkMixin(FormView):

    form_class = PostWorkerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def form_valid(self, form):
        worker = form.save(commit=False)
        worker.worker_type = self.service_type
        worker.save()

        messages.success(self.request, 'Форму успішно відправлено!')
        return super().form_valid(form)

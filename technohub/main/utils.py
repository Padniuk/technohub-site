import os
import json
from django.views.generic import FormView, ListView
from main.forms import PostApplicationForm, PostWorkerForm
from main.models import Service
from django.contrib import messages
import requests

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
        

        message_text = f"🔵 Aктивно\n\n{application.problem}\n\nАдреса: `{application.address}`"

        message_id = self.notify_telegram_bot(self.service_type, message_text)
        application.message_id = message_id

        application.save()
        messages.success(self.request, 'Форму успішно відправлено!')
        return super().form_valid(form)


    def notify_telegram_bot(self, service_type, message_text):
        bot_token = os.environ.get('BOT_TOKEN')

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

        inline_keyboard = [
            [{"text": "Взяти замовлення ", "callback_data": "send_customer_info"}]
        ]

        markup = {
            "inline_keyboard": inline_keyboard
        }

        inline_keyboard_json = json.dumps(markup)

        chat_id_map = {'electricity': os.environ.get('ELECTRICITY_CHAT_ID'), 'plumbing': os.environ.get('PLUMBING_CHAT_ID')}

        message_json = {
            'chat_id': chat_id_map.get(service_type),
            'text': message_text,
            'reply_markup': inline_keyboard_json,
            'parse_mode': 'Markdown'
        }

        response = requests.post(url, json=message_json)

        response_data = response.json()
        message_id = response_data.get('result', {}).get('message_id', None)
        return message_id
   


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

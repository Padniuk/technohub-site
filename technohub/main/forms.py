from django import forms
from main.models import Application, Worker


class PostApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["name", "phone", "problem", "address"]
        labels = {
            "name": "Ваше ім'я:",
            "phone": "Ваш телефон:",
            "problem": "Коротко опишіть суть вашої проблеми:",
            "address": "Ваша адреса:"
            
        }
        widgets = {
            'name': forms.TextInput(attrs={'type': "text", 'class': "form__input", 'placeholder': "Іван"}),
            'phone': forms.TextInput(attrs={'type': "text", 'class': "form__input", 'placeholder': "+38(066)-666-66-66"}),
            'address': forms.TextInput(attrs={'type': "text", 'class': "form__input", 'placeholder': "Київ, Здановської 48"}),
            "problem": forms.Textarea(attrs={'id': "problem", 'name': "problem", 'class': "form__input form__problem", 'cols': "30",'rows': "10", 'placeholder': "Несправність з ..."})
        }

class PostWorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ["name", "phone", "additional_info"]
        labels = {
            "name": "Ваше ім'я:",
            "phone": "Ваш телефон:",
            "additional_info": "Додаткова інформація:",
        }
        widgets = {
            'name': forms.TextInput(attrs={'type': "text", 'class': "form__input", 'placeholder': "Іван"}),
            'phone': forms.TextInput(attrs={'type': "text", 'class': "form__input", 'placeholder': "+38(066)-666-66-66"}),
            "additional_info": forms.Textarea(attrs={'id': "problem", 'name': "problem", 'class': "form__input form__problem", 'cols': "30",'rows': "10", 'placeholder': "Telegram, Viber"})
        }
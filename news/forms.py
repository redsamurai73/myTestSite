from django import forms
from django.core.exceptions import ValidationError

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'surname', 'telephoneNumber', 'message', 'file')

    def clean_telephoneNumber(self):
        data = self.cleaned_data['telephoneNumber']
        if (data < 10 ** 10) or (data >= 10 ** 11):
            raise ValidationError("Неверный номер телефона!")
        return data

    def clean_message(self):
        data = self.cleaned_data['message']
        if len(data) == 0:
            raise ValidationError("Пустое поле!")
        return data

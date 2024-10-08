from django.forms import ModelForm, BooleanField
from mailing.models import Mailing, Client, Message
from django.forms.widgets import DateTimeInput
class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"
        widgets = {
            'start_time': DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'end_time': DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'next_time_mailing': DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
        }



class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = "__all__"

class MailingManagerForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('active',)
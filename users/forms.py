from mailing.forms import StyleFormMixin, ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widger = forms.HiddenInput()


class ManagerChangeUserForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
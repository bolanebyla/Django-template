from .models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class AdminUserAddForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class AdminUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

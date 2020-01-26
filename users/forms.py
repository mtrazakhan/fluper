from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm


User = get_user_model()


class UserCreationForm(AuthUserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','job_role', 'user_type')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
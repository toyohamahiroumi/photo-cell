
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Photo
from users.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'icon')


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = {'image', 'comment', 'tags', }

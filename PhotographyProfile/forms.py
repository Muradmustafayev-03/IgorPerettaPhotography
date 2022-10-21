from django.contrib.auth.forms import UserCreationForm
from .models import User, Post
from django import forms

EMAIL = ''


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        if not user.is_owner:
            user.is_owner = False

        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=250)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'caption', 'tags']

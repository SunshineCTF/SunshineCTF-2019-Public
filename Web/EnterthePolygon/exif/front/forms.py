from django import forms
from front import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
""""
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
"""
class RegistrationForm(UserCreationForm):

	class Meta:
		model = User
		fields = {'username', 'password1', 'password2'}

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)

		if commit:
			user.save()

		return user

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.images
        fields = {'ifile'}
    ifile = forms.ImageField()

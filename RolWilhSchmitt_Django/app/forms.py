"""
Definition of forms.
"""

from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class FormattedDateField(models.DateField):
    widget = forms.DateInput(format='%d.%m.%Y')
    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%d.%m.%Y',)

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


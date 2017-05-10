from .models import Yeshiva, UpLoadToraText
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from pagedown.widgets import PagedownWidget

class AddYeshivaForm(forms.ModelForm):
    class Meta:
        model = Yeshiva
        exclude = ('user',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email', "password"]

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#not in use using create view in views
class UploadForm(forms.ModelForm):
    comment = forms.CharField(widget=PagedownWidget(show_preview=False))
    #date = forms.CharField(widget=forms.SelectDateWidget)
    class Meta:
        model = UpLoadToraText
        #fields = '__all__'
        fields = ["yeshiva","title","text","comment",]


class UpdateToraForm(forms.ModelForm):
    text = forms.CharField(widget=PagedownWidget(template='torasearch/read_text_pagedown.html'))
    #date = forms.CharField(widget=forms.SelectDateWidget)
    class Meta:
        model = UpLoadToraText
        #fields = '__all__'
        fields = ["text",]







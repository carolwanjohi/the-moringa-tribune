from django import forms

from django.contrib.auth.forms import AuthenticationForm
# from mediumeditor.widgets import MediumEditorTextarea
from .models import Article

class NewsLetterForm(forms.Form):
    '''
    Class to create a subscirption newsletter form 
    '''
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

class NewsArticleForm(forms.ModelForm):
    '''
    Class to create a form for an authenticated user to create an Article
    '''
    class Meta:
        model = Article
        exclude = ['editor','pub_date']
        widgets = {

            # 'post': forms.TimeInput(attrs={"col": 60, "row": 80}),
            'tags': forms.CheckboxSelectMultiple()
        }





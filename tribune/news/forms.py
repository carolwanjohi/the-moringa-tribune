from django import forms

class NewsLetterForm(forms.Form):
    '''
    Class to create a subscirption newsletter form 
    '''
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')




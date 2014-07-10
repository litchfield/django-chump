from django import forms

class ChumpSubscribeForm(forms.Form):
    name = forms.CharField(required=False, 
                widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(
                widget=forms.TextInput(attrs={'placeholder': 'Email address', 
                                              'required': True, 
                                              'type': 'email'}))

from mailchimp import utils
from django import forms

class ChumpSubscribeForm(forms.Form):
    name = forms.CharField(required=False, 
                widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(
                widget=forms.TextInput(attrs={'placeholder': 'Email address', 
                                              'required': True, 
                                              'type': 'email'}))

    def __init__(self, list_id, *args, **kwargs):
        self.list_id = list_id
        super(ChumpSubscribeForm, self).__init__(*args, **kwargs)

    def subscribe(self):
        d = self.cleaned_data
        lst = utils.get_connection().get_list_by_id(self.list_id)
        opt = {
            'EMAIL': d['email'],
            'NAME': d['name'],
        }
        lst.subscribe(d['email'], opt)


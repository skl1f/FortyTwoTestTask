from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=200,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    jabber = forms.CharField(max_length=75,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control'}))
    skype = forms.CharField(max_length=200,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    other_contact = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))

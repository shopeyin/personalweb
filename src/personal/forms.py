from django import forms

from personal.models import Contactus


class CreateMsgForm(forms.ModelForm):


    class Meta:
        model = Contactus
        fields = ['email','phonenumber','message']


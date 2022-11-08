from django.forms import ModelForm

from .models import Contact

from django import forms



class ContactForm(forms.ModelForm):

    name = forms.CharField( label='',
        widget = forms.TextInput(
        attrs={"class":"form-name",
               "placeholder" : "Name *",
    }))


    email = forms.CharField(label='',
        widget = forms.EmailInput(
        attrs={"class":"form-email",
               "placeholder" : "Email Address *",
    }))


    subject = forms.CharField(label='',
        widget = forms.TextInput(
        attrs={"class":"form-subject",
               "placeholder" : "Subject *",
    }))


    message = forms.CharField(label='',
        widget = forms.Textarea(
        attrs={"class":"form-message",
               "placeholder" : "Message *",
               "rows" : 5,
               "maxlength":350,
    }))


    class Meta:
        model = Contact
        fields = '__all__'


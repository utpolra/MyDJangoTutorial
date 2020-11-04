from django import forms
from django.forms import widgets
from .models import Contact,Post

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
class ContactFormtwo(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','id','created_at','slug']
        widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
            'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            })
        }
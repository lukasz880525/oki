from django import forms
#from .models import Message

# 2 sposób:

#class MessageForm(forms.ModelForm):
 #   class Meta:
  #      model= Message
   #     fields = ('name','email','message')

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())
# to jest i do 1 i do 2 sposobu:
    def clean_name(self):
        data = self.cleaned_data['name']
        if 'D' not in data:
            raise forms.ValidationError("musisz miec imie zawierajace ' D '!")
        return data
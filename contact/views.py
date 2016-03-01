from django.views.generic import DetailView,FormView
#from .models import Message
from .forms import ContactForm # MessageForm  # w 2 sposobie


# Create your views here.

# 2 sposób:

#class MessageDetailView(DetailView):
 #   model = Message

class MessageAddView(FormView):
    form_class = ContactForm # w 2 sposobie zamiast ContactForm musi byc MessageForm
    template_name = 'contact/message_form.html'
    success_url = '/'
# 2 sposób:
    #def form_valid(self, form):
     #   form.save()
     #   return super(MessageAddView, self).form_valid(form)
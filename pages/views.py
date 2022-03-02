from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('cont-success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'cont-success.html'
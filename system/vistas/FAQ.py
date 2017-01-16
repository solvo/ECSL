from django.views.generic import *
from system.models import *


class faq(ListView):
    template_name = 'faq/faq.html'
    queryset = Question.objects.filter(published=True).order_by('-created')
    context_object_name = 'faq_list'
	
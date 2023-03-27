from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Apartment
from .forms import ContactForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from django.http import JsonResponse


def get_expensive_app(self):
    template_name = 'lghter/index.py.html'
#        c = Apartment.objects.all().values_list()
#        counter = []
#        for elem in c:
#            x = 0
#            for f in elem:
#                if f is None:
#                    x = x + 1
#                endif
#            endfor
#            counter.append(x)
#     endfor
    x = 10
    return render(self, template_name, {'none_fields': x})

class IndexView(generic.ListView):
    template_name = 'lghter/index.html'
    model = Apartment
#    context_object_name = 'latest_question_list'

    def get_context_data(self):
        context = super().get_context_data()
        query = self.request.GET.get('q')
        # Additional context data
        counter = []
        p = Apartment.objects.order_by('-view_date')
        c = p.all().values_list()

        for elem in c:
            x = 0
            for f in elem:
                if f is None:
                    x = x + 1
            counter.append(x)
        context['x'] = counter
        context['latest_question_list'] = p
        context['expensive'] = Apartment.objects.order_by('-price_start')
        return context






 #   def get_queryset(self):
  #      """Return the last five published questions."""
  #      return Apartment.objects.order_by('-view_date')


class EditView(UpdateView):
    model = Apartment
    fields = '__all__'
    template_name = 'lghter/detail.html'
    success_url = '/'


class JsonableResponseMixin:
    """
    Mixin to add JSON support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            return JsonResponse(form.errors, status=400)

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            return response
        else:
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)


class NewView(CreateView):
    template_name = 'lghter/new.html'
    model = Apartment
    fields = '__all__'
    success_url = '/'

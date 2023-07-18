from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from main.forms import ClientForm
from main.models import Client


class ClientListView(LoginRequiredMixin, generic.ListView):
    model = Client
    template_name = 'main/clients/client_list.html'
    extra_context = {
        'title': 'Клиенты'
    }


class ClientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'main/clients/client_detail.html'
    success_url = reverse_lazy('main:clients')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class ClientCreateView(generic.CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'main/clients/client_form.html'
    success_url = reverse_lazy('main:clients')


class ClientDeleteView(generic.DeleteView):
    model = Client
    template_name = 'main/clients/client_confirm_delete.html'
    success_url = reverse_lazy('main:clients')
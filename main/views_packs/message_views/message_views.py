from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from main.forms import MessageForm
from main.models import Message


class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message
    template_name = 'main/message/message_list.html'
    extra_context = {
        'title': 'Список сообщений'
    }


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'main/message/message_form.html'
    success_url = reverse_lazy('main:message')


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'main/message/message_detail.html'
    success_url = reverse_lazy('main:message')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:message_update', kwargs={'pk': pk})


class MessageDeleteView(generic.DeleteView):
    model = Message
    template_name = 'main/message/message_confirm_delete.html'
    success_url = reverse_lazy('main:message')

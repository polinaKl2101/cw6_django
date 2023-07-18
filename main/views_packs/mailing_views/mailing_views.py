from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from main.forms import MailingForm
from main.models import Mailing
from main.services import send_mail


class MailingListView(LoginRequiredMixin, generic.ListView):
    model = Mailing
    template_name = 'main/mailing/mailing_list.html'
    extra_context = {
        'title': 'Список рассылок'
    }


class MailingCreateView(generic.CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/mailing/mailing_form.html'
    success_url = reverse_lazy('main:mailing')

    def form_valid(self, form):
        form.instance.status = 'running'
        response = super().form_valid(form)
        send_mail(self.object)
        return response

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        mailing = self.object
        mailing.status = 'running'
        mailing.save()
        send_mail(mailing)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mailing_number'] = Mailing.objects.count()
        return context


class MailingDetailView(generic.DetailView):
    model = Mailing
    template_name = 'main/mailing/mailing_detail.html'


class MailingUpdateView(generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'main/mailing/mailing_update.html'
    success_url = reverse_lazy('main:mailing')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:update_mailing', kwargs={'pk': pk})


class MailingDeleteView(generic.DeleteView):
    model = Mailing
    template_name = 'main/mailing/mailing_confirm_delete.html'
    success_url = reverse_lazy('main:mailing')

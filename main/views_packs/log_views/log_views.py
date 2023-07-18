from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from main.models import Log
from main.services import get_cache_log


class LogListView(LoginRequiredMixin, generic.ListView):
    model = Log
    template_name = 'main/log/log_list.html'
    extra_context = {
        'title': 'Логи'
    }


class LogDetailView(generic.DetailView):
    model = Log
    template_name = 'main/log/log_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_data'] = get_cache_log(self.object)
        return context
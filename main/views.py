from django.db.models import Count
from django.shortcuts import render
from django.views import generic

from main.models import Mailing, Client, BlogPost


def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html')


class IndexView(generic.ListView):
    def get(self, request, *args, **kwargs):
        mailing_number = Mailing.objects.count()
        mailing_number_active = Mailing.objects.filter(
            status='running').count()
        unique_clients = Client.objects.annotate(mailing_num=Count('mailings')).filter(
            mailing_num__gt=0).count()
        blogpost = list(BlogPost.objects.filter(is_published=True).values_list('title', flat=True)[
                        :3])
        context = {
            'title': 'Сервис рассылок',
            'mailing_number': mailing_number,
            'mailing_number_active': mailing_number_active,
            'unique_clients': unique_clients,
            'blogpost': blogpost
        }
        return render(request, 'main/index.html', context)
from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import IndexView
from main.views_packs.blogpost_views.blogpost_views import BlogPostListView, BlogPostCreateView, BlogPostDetailView, \
    BlogPostDeleteView, BlogPostUpdateView
from main.views_packs.client_views.client_views import ClientCreateView, ClientListView, ClientDeleteView, \
    ClientUpdateView
from main.views_packs.message_views.message_views import MessageListView, MessageCreateView, MessageDeleteView, \
    MessageUpdateView
from main.views_packs.mailing_views.mailing_views import MailingListView, MailingCreateView, MailingUpdateView, \
    MailingDetailView, MailingDeleteView
from main.views_packs.log_views.log_views import LogListView, LogDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='index'),

    path('blogpost/', BlogPostListView.as_view(), name='blogpost'),
    path('blogpost/create', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('blogpost/detail/<int:pk>/', BlogPostDetailView.as_view(), name='detail_blogpost'),
    path('blogpost/update/<int:pk>/', BlogPostUpdateView.as_view(), name='update_blogpost'),
    path('blogpost/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blogpost'),

    path('clients/', ClientListView.as_view(), name='clients'),
    path('clients/create', ClientCreateView.as_view(), name='create_client'),
    path('clients/update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('clients/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('message/', MessageListView.as_view(), name='message'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('mailing/', MailingListView. as_view(), name='mailing'),
    path('mailing/create/', MailingCreateView. as_view(), name='create_mailing'),
    path('mailing/detail/<int:pk>/', MailingDetailView. as_view(), name='detail_mailing'),
    path('mailing/update/<int:pk>/', MailingUpdateView. as_view(), name='update_mailing'),
    path('mailing/delete/<int:pk>/', MailingDeleteView. as_view(), name='delete_mailing'),
    #
    path('log/', LogListView.as_view(), name='log'),
    path('log/detail/<int:pk>/', LogDetailView.as_view(), name='detail_log'),

]

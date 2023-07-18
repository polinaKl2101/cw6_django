from django.contrib import admin

from main.models import Log, Mailing, Message, Client, BlogPost


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('message', 'timedata', 'status')
    list_filter = ('message', 'timedata', 'status')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'mail_body', 'frequency', 'status')
    list_filter = ('frequency', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'mailing')
    list_filter = ('title', 'mailing')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname')
    list_filter = ('email', 'fullname')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published')

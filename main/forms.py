from django import forms

from main.models import BlogPost, Client, Message, Mailing, Log


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['email', 'fullname', 'comment']


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('title', 'mailing')


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ['title', 'mail_body', 'frequency', 'status', 'clients']


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview', 'is_published']


class StyleFormMixin:
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='Контактный email', unique=True)
    fullname = models.CharField(max_length=50, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):

        return f'{self.email}'

    class Meta:

        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):

    FREQUENCY_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )

    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('running', 'Запущена'),
        ('completed', 'Завершена'),
    )

    title = models.CharField(max_length=60, verbose_name='Тема рассылки')
    mail_body = models.TextField(verbose_name='Тело письма')
    frequency = models.CharField(max_length=25, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='created', verbose_name='Статус рассылки')
    clients = models.ManyToManyField('Client', verbose_name='Клиенты', related_name='mailings')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):

    title = models.CharField(max_length=25, verbose_name='Тема рассылки')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Log(models.Model):

    STATUS_CHOICES = (
        ('success', 'Успешно'),
        ('error', 'Ошибка'),
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение рассылки')
    timedata = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, verbose_name='Статус попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера')

    def __str__(self):
        return f"Время рассылки: {self.timedata}"

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"


class BlogPost(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(verbose_name='Текст поста')
    preview = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
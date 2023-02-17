from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=100, null=False, blank=False, verbose_name='Статус')
    created_at = models.TextField(max_length=3000, verbose_name='Дата')

    def __str__(self):
        return f'{self.title} - {self.description} - {self.status} - {self.created_at}'

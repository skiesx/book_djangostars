from django.db import models
from datetime import datetime
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class Book(models.Model):
    title = models.CharField(max_length = 140)
    author = models.CharField(max_length = 250)
    isbn = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    publish_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

class WebRequest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    data = models.TextField()

    def __str__(self):
        return self.title

class LogBook(models.Model):
    action_time = models.DateTimeField(auto_now_add=True)
    object_id = models.TextField()
    object_title = models.TextField()
    action_flag = models.CharField(max_length = 50)


@receiver(post_save, sender = Book)
def add_log_create_update(instance, **kwargs):
    if kwargs['created']:
        LogBook.objects.create(object_id = instance.id, object_title = instance.title, action_flag = "create")
    else:
        LogBook.objects.create(object_id = instance.id, object_title = instance.title, action_flag = "update")

@receiver(pre_delete, sender = Book)
def add_log_delete(instance, **kwargs):
    LogBook.objects.create(object_id = instance.id, object_title = instance.title, action_flag = "delete")

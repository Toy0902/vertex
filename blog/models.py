from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class Rasmlar(models.Model):
    nomi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasm/images')
    def __str__(self):
        return self.nomi
class Matn(models.Model):
    nomi = models.CharField(max_length=200)
    rasm = models.ImageField(upload_to='rasm/images')
    text = models.TextField()
    chopetilish_vaqti = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-chopetilish_vaqti']
    object = models.Manager()

class Comment(models.Model):
    product = models.ForeignKey(Matn,
                                on_delete=models.CASCADE,
                                related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comments -{self.body} by {self.user}"



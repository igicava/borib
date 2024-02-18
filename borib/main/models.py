from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='images_news', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # При создании нового объекта устанавливаем начальное значение поля
            self.date = timezone.now()
        return super(News, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} : {self.date}'

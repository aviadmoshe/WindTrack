from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Yeshiva(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    rav_name = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 1000)
    date = models.DateTimeField(auto_now_add=True , null = True)

    def get_absolute_url(self):
        return reverse('detail',kwargs = {'pk':self.pk})

    def __str__(self):
        return self.name + '-' + self.rav_name
    

class UpLoadToraText(models.Model):
    yeshiva = models.ForeignKey(Yeshiva,related_name='yeshiva',on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.FileField(null=True, blank=True)
    comment = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True, null = True)

    def get_absolute_url(self):
        return reverse('detail',kwargs = {'pk':self.yeshiva.pk})

    def __str__(self):
        return self.text.name
   









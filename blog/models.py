from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_title = models.DateTimeField('date published')
    body = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body
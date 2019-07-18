from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Bug(models.Model):
    STATUS = (
            ('T', 'To Do'),
            ('P', 'In Progress'),
            ('C', 'Complete')
        )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default='0')
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS, default='T')

    def __str__(self):
        return self.name
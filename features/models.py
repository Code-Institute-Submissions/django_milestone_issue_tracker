from django.db import models
from django.contrib.auth.models import User


class Feature(models.Model):
    STATUS = (
            ('T', 'To Do'),
            ('P', 'In Progress'),
            ('C', 'Complete')
        )
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    vote_price = models.DecimalField(default=5, max_digits=6, decimal_places=2)
    quantity = models.DecimalField(max_digits=1, decimal_places=0, default='1')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default='0')
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=1, choices=STATUS, default='T')

    def __str__(self):
        return self.name


class UpvoteFeature(models.Model):
    upvoted_feature = models.ForeignKey(Feature, default=None,
                                        on_delete=models.CASCADE)
    user_voted = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class CommentFeature(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.user)

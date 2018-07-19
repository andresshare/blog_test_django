from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Post(models.model):
    author = models.ForeignKey('auth.User')
    title  = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    create_date = models.DateTimeField(defaukt=timezone.now())
    published_date = models.DateTimeField(blank=True, null=true)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def __str__(self):
        return self.title

class Comment(model.Models):
    post = models.ForeignKey('blog.POST', related_name='comments')
    author = models.CharField(max_length="200")
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
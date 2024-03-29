from asyncio import proactor_events
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    like_user_set = models.ManyToManyField(User, blank=True, related_name='likes_user_set', through='Like')
    dislike_user_set = models.ManyToManyField(User, blank=True, related_name='dislike_user_set', through='Dislike')
    
    @property
    def like_count(self):
        return self.like_user_set.count()

    @property
    def dislike_count(self):
        return self.dislike_user_set.count()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user','post'))

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user', 'post'))
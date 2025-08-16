from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def add_comment(self, author, text):
        comment = Comment.objects.create(post=self, author=author, text=text)
        return comment

    def edit_post(self, title=None, content=None):
        if title:
            self.title = title
        if content:
            self.content = content
        self.save()
        return self


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"

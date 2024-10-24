from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):

    post = models.ForeignKey(
        Post, related_name='sections', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200)  # Subtitle for each section
    content = models.TextField()  # Content for each section

    def __str__(self):
        return f"{self.subtitle} (Post: {self.post.title})"

from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length= 100)
    post = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='uploads/')
    author = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return f"/templates/{self.id}/"
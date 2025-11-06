from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=50)
    status=models.BooleanField()
    body=models.TextField()
    created_at=models.TimeField(auto_now_add=True)
    Images=models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'{self.title}'



from django.db import models

class About (models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    file = models.FileField(upload_to='about_files/')

    def str(self):
        return self.title

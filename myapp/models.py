from django.db import models

class PowerPointTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_file = models.FileField(upload_to='ppt_templates/')
    thumbnail = models.ImageField(upload_to='ppt_thumbnails/')  # Path for thumbnails

    def __str__(self):
        return self.name




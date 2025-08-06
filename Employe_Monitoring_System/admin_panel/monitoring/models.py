from django.db import models

# Create your models here.
def user_directory_path(instance,filename):
    return f"screenshots/{instance.username}/{filename}"
class ScreenshotLog(models.Model):
    username = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to=user_directory_path)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    device_info = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.timestamp}"
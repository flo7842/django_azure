from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

def validate_unique_textfield(value):
    if Image.objects.filter(base64=value).exists():
        raise ValidationError(('This value already exists.'))

class Image(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    tags = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    base64 = models.TextField(blank=True, null=True, validators=[validate_unique_textfield])
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name
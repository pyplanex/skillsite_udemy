from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
# Create your models here.


class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='uploads/img', validators=[
                               FileExtensionValidator(allowed_extensions=['png'])], blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def get_created(self):
        return self.created.strftime("%m/%d/%Y, %H:%M:%S")

    def __str__(self):
        return "{}-{}".format(self.name, self.get_created)

from django.db import models
from django.contrib.auth.hashers import make_password, check_password

from django.utils import timezone
# Create your models here.
class UserDetails(models.Model):

    name = models.CharField()
    email = models.EmailField()
    address = models.CharField()
    password = models.CharField()
    last_login = models.DateTimeField(null=False, default=timezone.now)
    role = models.CharField(default='user')

    def save(self, *args, **kwargs):
        if not self.password.startswith("pbk"):
            self.password = make_password(self.password)  # before saving the password, im hasihing the password
        super().save(*args, **kwargs)

    def check_password_User(self, entered_password):
        # print(entered_password)

        return check_password(entered_password, self.password)
    def __str__(self):
        return self.name
from django.db import models


class User(models.Model):
    user_phone_num = models.CharField(unique=True, max_length=13, blank=False)
    user_name = models.CharField(max_length=128, blank=False)
    user_address = models.CharField(max_length=128, null=True)
    user_password = models.CharField(max_length=256, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-update_date']
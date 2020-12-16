from django.db import models



class MyUsers(models.Model):
    name = models.CharField("Name", max_length=150)
    email = models.EmailField("Email", max_length=254, blank=True)
    phone = models.CharField("Phone", max_length=20)
    created_at = models.DateTimeField(
        "Created At", auto_now_add=True, null=True)

    def __str__(self):
        return self.name
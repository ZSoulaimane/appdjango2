from django.db import models

# Create your models here.
class authentification_users(models.Model):
    username = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)

    class meta:
        db_table = "authentification_users"
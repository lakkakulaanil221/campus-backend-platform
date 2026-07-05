from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email= models.EmailField(unique=True)
    phone_number= models.CharField(max_length=10)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "users"
        ordering= ["-created_at"]

    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username}"
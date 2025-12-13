from uuid import uuid4
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from .utils import get_original_upload_path, get_processed_upload_path


class AssetType(models.TextChoices):
    IMAGE = "image", "Image"
    VIDEO = "video", "Video"
    AUDIO = "audio", "Audio"


class AssetStatus(models.TextChoices):
    PROCESSING = "processing", "Processing"
    FAILED = "failed", "Failed"
    COMPLETED = "completed", "Completed"


class Asset(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid4, unique=True, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="assets", on_delete=models.CASCADE, null=True, blank=True
    )
    status = models.CharField(
        max_length=20, choices=AssetStatus.choices, default=AssetStatus.PROCESSING
    )

    original_image = models.FileField(upload_to=get_original_upload_path, max_length=500)
    processed_image = models.FileField(upload_to=get_processed_upload_path, blank=True, null=True, max_length=500)

    name = models.CharField(max_length=255)
    size = models.BigIntegerField()
    asset_type = models.CharField(max_length=10, choices=AssetType.choices)
    
    metadata = models.JSONField(verbose_name="Asset metadata", blank=True, null=True)

    is_visible = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)

    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        user_display = self.user.username if self.user else 'N/A'
        return f"{user_display} - Asset"

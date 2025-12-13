from rest_framework import serializers
from .models import Asset

class AssetListSerializer(serializers.ModelSerializer):
    
    uploaded_at = serializers.DateTimeField(source="created_at")
    asset_url = serializers.FileField(source="original_image", read_only=True)
    
    class Meta:
        model = Asset
        fields = ['name', 'size', 'asset_type', 'uploaded_at', 'asset_url', 'uuid']
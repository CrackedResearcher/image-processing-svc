from django.urls import path
from .views import UploadMediaView, UploadedAssetListView, ImageTransformView, ImageDetailView

urlpatterns = [
    path("upload/", UploadMediaView.as_view(), name="media-upload-view"),
    path("images/<uuid:id>/transform/", ImageTransformView.as_view(), name="image-transform-view"),
    path("images/<uuid:id>/", ImageDetailView.as_view(), name="image-detail-view"),
    path("list/", UploadedAssetListView.as_view(), name="asset-list-view")
]
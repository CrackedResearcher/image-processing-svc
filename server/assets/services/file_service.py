from ..models import Asset
from .exceptions import InvalidAssetError

def _extract_metadata(file):
    """
    extracts metadata from the given file and returns a dict
    """
    
    name, size, content_type = file.name, file.size, file.content_type
    file_type = content_type.split('/')[0]
    allowed_types = ["image", "video", "audio"]
    if file_type not in allowed_types:
        raise InvalidAssetError(f"Type '{file_type}' is not supported. only image, video, or audio.")

    return {
        "name": name,
        "size": size,
        "asset_type": file_type
    }
    
    
def process_and_save_file(file, user):
    file_dict = _extract_metadata(file)
    asset_obj = Asset.objects.create(
        user=user,
        name=file_dict['name'],
        size=file_dict['size'],
        asset_type=file_dict['asset_type'],
        original_image=file
    )
    return asset_obj

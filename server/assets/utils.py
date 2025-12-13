import os
from datetime import datetime

def _generate_base_path(instance, filename, category):
    """
    internal logic to generate path based on category ('original-images' or 'processed-images')
    """
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    
    file_root, ext = os.path.splitext(filename)
    
    visibility = "public" if instance.is_public else "private"
    
    if instance.user:
        owner_path = f"user-{instance.user.uuid}"
    else:
        owner_path = "platform"

    clean_name = instance.name if instance.name else file_root
    
    return f"{owner_path}/{visibility}/{instance.asset_type}/{category}/{timestamp}-{clean_name}"


def get_original_upload_path(instance, filename):
    return _generate_base_path(instance, filename, 'original-images')

def get_processed_upload_path(instance, filename):
    return _generate_base_path(instance, filename, 'processed-images')
from ast import Assert
from ..models import Asset
from .exceptions import InvalidAssetError

def get_asset_list(user):
    asset_list = Asset.objects.filter(user=user)
    return asset_list
    
def get_asset_detail(user, id):
    try:
        return Asset.objects.get(user=user, uuid=id)
    except Asset.DoesNotExist:
        # Raise an error or return None, depending on how your view handles it
        raise InvalidAssetError(f"No asset with {id} found.")
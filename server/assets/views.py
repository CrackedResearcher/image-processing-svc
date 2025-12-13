from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from assets.services.exceptions import InvalidAssetError

from .serializers import AssetListSerializer
from .services import assets, file_service


class UploadMediaView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request: Request):
        user = request.user
        file = request.FILES.get("file")
        if not file:
            return Response(
                {"error": "at least one image is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            asset = file_service.process_and_save_file(file, user)
            return Response(
                {
                    "id": asset.uuid,
                    "message": "file uploaded successfully",
                    "type": asset.asset_type,
                },
                status=status.HTTP_201_CREATED,
            )

        except InvalidAssetError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Internal Error: {e}")
            return Response(
                {"error": "Something went wrong processing the file."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class UploadedAssetListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AssetListSerializer

    def get_queryset(self):
        return assets.get_asset_list(self.request.user)


class ImageTransformView(APIView):
    pass


class ImageDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AssetListSerializer

    def get(self, request, id):
        user = request.user
        try:
            asset_data = assets.get_asset_detail(user, id)
            data = AssetListSerializer(asset_data).data
            return Response({"data": data}, status=status.HTTP_200_OK)
        except InvalidAssetError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {"error": "Something went wrong processing the file."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

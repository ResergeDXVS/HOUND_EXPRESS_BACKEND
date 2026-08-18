from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Package
from .serializers import PackageSerializers

class CreateGuideView(APIView):
    def post(self, request):
        serializer = PackageSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateGuideView(APIView):
    def put(self, request, pk):
        try:
            package = Package.objects.get(pk=pk)
        except Package.DoesNotExist:
            return Response({"error": "Guía no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PackageSerializers(package, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetGuideView(APIView):
    def get(self, request, pk):
        try:
            package = Package.objects.get(pk=pk)
        except Package.DoesNotExist:
            return Response({"error": "Guía no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PackageSerializers(package)
        return Response(serializer.data)


class DeleteGuideView(APIView):
    def delete(self, request, pk):
        try:
            package = Package.objects.get(pk=pk)
        except Package.DoesNotExist:
            return Response({"error": "Guía no encontrada"}, status=status.HTTP_404_NOT_FOUND)

        package.delete()
        return Response({"message": f"Guía {pk} eliminada"}, status=status.HTTP_204_NO_CONTENT)

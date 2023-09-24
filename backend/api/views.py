from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from files.models import File
from .serializers import FileSerializer
from .tasks import task


class UploadViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        obj = serializer.save()
        task(obj)


class FileViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
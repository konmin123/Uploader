from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from files.models import File
from .serializers import FileSerializer


class UploadViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    http_method_names = ['post']

    def perform_create(self, serializer):
        # запуск ассинхронной задачи обработки через celary
        serializer.save()


class FileViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
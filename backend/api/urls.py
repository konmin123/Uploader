from django.urls import include, path
from rest_framework import routers

from .views import FileViewSet
from .views import UploadViewSet

router = routers.DefaultRouter()
router.register('upload', UploadViewSet)
router.register('files', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

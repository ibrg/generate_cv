from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CvViewSet


router = DefaultRouter()
router.register('cv_list', CvViewSet)


urlpatterns = [
    path('', include(router.urls))
]

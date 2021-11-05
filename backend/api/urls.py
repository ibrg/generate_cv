from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CvViewSet, WorkViewSet


router = DefaultRouter()
router.register('cv_list', CvViewSet),
router.register('work', WorkViewSet)


urlpatterns = [
    path('', include(router.urls))
]

from rest_framework import viewsets
from app_cv.models import CV
from api.serializers import CVSerializers


class CvViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializers

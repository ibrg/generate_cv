from rest_framework import viewsets
from app_cv.models import CV, WorkExperience
from api.serializers import CVSerializers, WorkSerializer


class CvViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializers


class WorkViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkSerializer

from rest_framework import serializers

from app_cv.models import CV


class CVSerializers(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'

from rest_framework import serializers

from app_cv.models import CV, WorkExperience, Education


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ('company_name', 'work_position', 'work_start', 'work_end', 'work_now', 'description',)

    def create(self, validated_data):
        print(validated_data)

        ser = WorkExperience.objects.create(**validated_data)
        ser.save()
        return ser


class EducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('education_name', 'education_start', 'education_end', 'studying_now',)


class CVSerializers(serializers.ModelSerializer):
    work_experience = WorkSerializer(many=True, required=False)
    education = EducationSerializers(many=True, required=False)

    class Meta:
        model = CV
        fields = ['title', 'fullname', 'english', 'email', 'linkedin', 'github', 'contact', 'skills', 'description',
                  'awards', 'work_experience', 'education']

    def create(self, validated_data):
        work_data = edu_data = []
        if 'work_experience' in validated_data:
            work_data = [WorkExperience.objects.create(**job) for job in validated_data.pop('work_experience')]

        if 'education' in validated_data:
            edu_data = [Education.objects.create(**edu) for edu in validated_data.pop('education')]

        serializer = CV.objects.create(**validated_data)

        if work_data != '':
            serializer.work_experience.set(work_data)

        if edu_data != '':
            serializer.education.set(edu_data)

        serializer.save()
        return serializer

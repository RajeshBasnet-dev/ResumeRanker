from rest_framework import serializers
from .models import JobDescription, Resume

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ['id', 'title', 'description', 'created_at']

class ResumeSerializer(serializers.ModelSerializer):
    file = serializers.FileField(write_only=True)
    score = serializers.FloatField(read_only=True)
    file_url = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = ['id', 'job', 'file', 'file_url', 'score', 'uploaded_at']

    def get_file_url(self, obj):
        return obj.file.url if obj.file else None

    def validate_file(self, value):
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError("Only PDF files are allowed.")
        return value
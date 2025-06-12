from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobDescription, Resume
from .serializers import JobDescriptionSerializer, ResumeSerializer
from .analyzer import extract_text_from_pdf, calculate_resume_score
from django.shortcuts import get_object_or_404

class JobDescriptionListCreateView(APIView):
    def get(self, request):
        jobs = JobDescription.objects.all()
        serializer = JobDescriptionSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobDescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JobDescriptionDetailView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(JobDescription, id=job_id)
        serializer = JobDescriptionSerializer(job)
        return Response(serializer.data)

class ResumeUploadView(APIView):
    def post(self, request, job_id):
        job = get_object_or_404(JobDescription, id=job_id)
        files = request.FILES.getlist('resumes')
        if not files:
            return Response({"error": "No resumes uploaded."}, status=status.HTTP_400_BAD_REQUEST)

        responses = []
        for file in files:
            data = {'job': job.id, 'file': file}
            serializer = ResumeSerializer(data=data)
            if serializer.is_valid():
                resume = serializer.save()
                resume_text = extract_text_from_pdf(resume.file.path)
                score = calculate_resume_score(resume_text, job.description)
                resume.score = score
                resume.save()
                responses.append(ResumeSerializer(resume).data)
            else:
                responses.append(serializer.errors)

        return Response(responses, status=status.HTTP_201_CREATED)

class ResumeRankView(APIView):
    def get(self, request, job_id):
        job = get_object_or_404(JobDescription, id=job_id)
        resumes = job.resumes.all().order_by('-score')
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)
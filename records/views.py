from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import ReportCardSerializer


class StudentReportCardView(APIView):
    def get(self, request, student_id: int):
        student = get_object_or_404(
            Student.objects.select_related("school_class").prefetch_related(
                "marks__subject"
            ),
            pk=student_id,
        )
        serializer = ReportCardSerializer(student)
        return Response(serializer.data)

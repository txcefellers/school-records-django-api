from rest_framework import serializers

from .models import Mark, Student


class ReportCardMarkSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source="subject.name")
    subject_code = serializers.CharField(source="subject.code")

    class Meta:
        model = Mark
        fields = ("subject", "subject_code", "exam_name", "score")


class ReportCardSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    class_name = serializers.SerializerMethodField()
    marks = ReportCardMarkSerializer(many=True, read_only=True)
    total_score = serializers.SerializerMethodField()
    average_score = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = (
            "id",
            "admission_number",
            "student_name",
            "class_name",
            "marks",
            "total_score",
            "average_score",
        )

    def get_student_name(self, obj: Student) -> str:
        return f"{obj.first_name} {obj.last_name}"

    def get_class_name(self, obj: Student) -> str:
        return str(obj.school_class)

    def get_total_score(self, obj: Student) -> float:
        return float(sum(mark.score for mark in obj.marks.all()))

    def get_average_score(self, obj: Student) -> float:
        marks = list(obj.marks.all())
        if not marks:
            return 0.0
        return round(float(sum(mark.score for mark in marks) / len(marks)), 2)

from django.contrib import admin
from .models import Mark, SchoolClass, Student, Subject


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ("name", "section")
    search_fields = ("name", "section")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("admission_number", "first_name", "last_name", "school_class")
    list_filter = ("school_class",)
    search_fields = ("admission_number", "first_name", "last_name")


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "exam_name", "score", "recorded_at")
    list_filter = ("exam_name", "subject")
    search_fields = (
        "student__first_name",
        "student__last_name",
        "student__admission_number",
        "subject__name",
        "subject__code",
    )

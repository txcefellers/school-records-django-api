from django.db import models


class SchoolClass(models.Model):
    name = models.CharField(max_length=100, unique=True)
    section = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ["name", "section"]
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self) -> str:
        if self.section:
            return f"{self.name} - {self.section}"
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.code} ({self.name})"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=40, unique=True)
    school_class = models.ForeignKey(
        SchoolClass, on_delete=models.PROTECT, related_name="students"
    )

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.admission_number})"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, related_name="marks")
    score = models.DecimalField(max_digits=5, decimal_places=2)
    exam_name = models.CharField(max_length=100, default="Final")
    recorded_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["subject__name"]
        unique_together = ("student", "subject", "exam_name")

    def __str__(self) -> str:
        return f"{self.student} - {self.subject.code}: {self.score}"

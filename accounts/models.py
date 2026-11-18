from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    college = models.CharField(max_length=150)
    graduation_year = models.IntegerField()
    skills = models.TextField()
    experience = models.CharField(max_length=50)
    job_role = models.CharField(max_length=100)
    expected_salary = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Company(models.Model):
    company_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True)
    industry = models.CharField(max_length=100)
    company_size = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.company_name


class Job(models.Model):
    job_title = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    company_name = models.CharField(max_length=150)
    job_description = models.TextField()
    requirements = models.TextField()
    salary = models.IntegerField()
    job_location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    experience_required = models.CharField(max_length=50)
    qualification_required = models.CharField(max_length=100)
    skills_required = models.TextField()
    vacancies = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title


class Application(models.Model):

    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    applied_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    def __str__(self):
        return f"{self.student} - {self.job}"
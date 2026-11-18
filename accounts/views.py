from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages

from .models import Job, Application, Student
from .forms import StudentRegistrationForm


# 1. Job Listing and Search
def job_list(request):

    search_query = request.GET.get('search', '')

    jobs = Job.objects.filter(is_active=True)

    if search_query:
        jobs = jobs.filter(
            Q(job_title__icontains=search_query) |
            Q(job_location__icontains=search_query) |
            Q(company_name__icontains=search_query)
        )

    return render(request, 'accounts/job_list.html', {
        'jobs': jobs,
        'search_query': search_query
    })


# 2. Job Details
def job_detail(request, job_id):

    job = get_object_or_404(Job, id=job_id, is_active=True)

    return render(request, 'accounts/job_detail.html', {
        'job': job
    })


# 3. Student Registration
def student_register(request):

    if request.method == "POST":

        form = StudentRegistrationForm(request.POST)

        if form.is_valid():

            student = form.save()

            request.session['student_id'] = student.id

            messages.success(
                request,
                "Registration completed successfully!"
            )

            return redirect('job_list')

    else:
        form = StudentRegistrationForm()

    return render(request, 'accounts/student_register.html', {
        'form': form
    })


# 4. Apply for Job
def apply_job(request, job_id):

    if request.method == "POST":

        job = get_object_or_404(Job, id=job_id, is_active=True)

        student_id = request.session.get('student_id')

        student = Student.objects.filter(id=student_id).first()

        if student:

            application, created = Application.objects.get_or_create(
                student=student,
                job=job
            )

            if created:
                messages.success(
                    request,
                    "Application submitted successfully!"
                )
            else:
                messages.warning(
                    request,
                    "You have already applied for this job."
                )

        else:
            messages.error(
                request,
                "Please register as a student first."
            )

        return redirect('job_list')

    return redirect('job_detail', job_id=job_id)


# 5. My Applications
def my_applications(request):

    student_id = request.session.get('student_id')

    applications = Application.objects.filter(
        student_id=student_id
    ).select_related(
        'student', 'job'
    ).order_by('-applied_at')

    return render(request, 'accounts/my_applications.html', {
        'applications': applications
    })
from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'first_name',
            'last_name',
            'email',
            'age',
            'gender',
            'phone',
            'date_of_birth',
            'city',
            'state',
            'country',
            'pincode',
            'qualification',
            'specialization',
            'college',
            'graduation_year',
            'skills',
            'experience',
            'job_role',
            'expected_salary',
            'address',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'address': forms.Textarea(
                attrs={'rows': 3}
            ),

            'skills': forms.Textarea(
                attrs={'rows': 3}
            ),
        }
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm, forms.ModelForm):
    """Login form"""

    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-login'


class CurriculumForm(forms.ModelForm):
    """Form curriculum"""

    class Meta:
        model = Curriculum
        fields = ("creator", "title", "year_of_start", "year_of_end", "academic_level", "years_to_study",
                  "university_abbreviation", "faculty", "department",
                  "branch_of_knowledge", "speciality", "education_program", "speciality_addition_info",
                  "subjects", "form_education", "citizenship", "language_institution", "enrollment_number")


from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import User, Curriculum, Feedback  # Add import Feedback
from crispy_forms.helper import FormHelper  # Add import FormHelper
from crispy_forms.layout import Submit  # Add import Submit


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


# Add Feedback from
class FeedbackForm(forms.ModelForm):
    """Form feedback"""

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите электронный адрес'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тему'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите сообщение'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Отправить сообщение'))

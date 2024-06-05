from bootstrap_modal_forms.generic import BSModalFormView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.views.generic.base import View
from django.views.generic.detail import SingleObjectMixin

from .models import UniversityTeacher, Curriculum, Feedback  # Add import Feedback
from .forms import LoginUserForm, CurriculumForm, FeedbackForm  # Add import FeedbackForm
from django.core.mail import send_mail  # Add import send_mail
from django.conf import settings  # Add import settings
import requests


# =====| HOME |=====

class HomeView(LoginRequiredMixin, ListView):
    """Home page"""

    model = Curriculum
    queryset = Curriculum.objects.all()
    template_name = "curriculum_ms/home.html"
    context_object_name = "curriculums"

    def get_context_data(self, **kwargs):
        kwargs['curriculums'] = Curriculum.objects.order_by('-date_last_changed')[:5]
        kwargs['curriculum_count'] = Curriculum.objects.all().count()
        kwargs['teachers'] = UniversityTeacher.objects.all()
        return super().get_context_data(**kwargs)


# =====| AUTH |=====

class SignInView(LoginView):
    """Sign in page"""

    template_name = 'curriculum_ms/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url


class LogoutView(TemplateView):
    """Sing out page"""

    template_name = 'curriculum_ms/login.html'
    success_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


# =====| PAGE |=====

class CreateCurriculumView(LoginRequiredMixin, TemplateView):
    """Create curriculum page"""

    template_name = "curriculum_ms/create_curriculum.html"

    def get_context_data(self, **kwargs):
        kwargs['creator'] = self.request.user.id
        return super().get_context_data(**kwargs)


class ListCurriculumView(LoginRequiredMixin, ListView):
    """List curriculums page"""

    model = Curriculum
    queryset = Curriculum.objects.all()
    template_name = "curriculum_ms/list_curriculums.html"
    context_object_name = "curriculums"

    def get_context_data(self, **kwargs):
        kwargs['curriculums'] = Curriculum.objects.order_by('date_last_changed')  # ORDER BY !!!
        return super().get_context_data(**kwargs)


class SearchCurriculumView(LoginRequiredMixin, ListView):
    """Search curriculum page"""

    model = Curriculum
    queryset = Curriculum.objects.all()
    template_name = "curriculum_ms/search_curriculum.html"
    context_object_name = "curriculums"

    def get_context_data(self, **kwargs):
        kwargs['curriculums'] = Curriculum.objects.all()  # FILTER !!!
        return super().get_context_data(**kwargs)


class DetailCurriculumView(LoginRequiredMixin, DetailView):
    """Detail Curriculum page"""

    model = Curriculum
    slug_field = "id"
    template_name = "curriculum_ms/detail_curriculum.html"
    context_object_name = "curriculum"

    def get_context_data(self, **kwargs):
        kwargs['creator'] = self.request.user.id
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        return self.model.objects.filter(id=self.kwargs['pk'])


class EditCurriculumView(LoginRequiredMixin, DetailView):
    """Edit Curriculum page"""

    model = Curriculum
    slug_field = "id"
    template_name = "curriculum_ms/edit_curriculum.html"


# class ContactView(LoginRequiredMixin, TemplateView):
#     """Contact page"""
#     template_name = "curriculum_ms/contact.html"


# =====| FORM |=====

class CreatedCurriculumView(LoginRequiredMixin, CreateView):
    model = Curriculum
    form_class = CurriculumForm
    success_url = reverse_lazy("home")
    template_name = "curriculum_ms/create_curriculum.html"


class UpdatedCurriculumView(LoginRequiredMixin, UpdateView):
    model = Curriculum
    form_class = CurriculumForm
    success_url = reverse_lazy("list_curriculums")
    template_name = "curriculum_ms/list_curriculums.html"


class ModalView(LoginRequiredMixin, DetailView):
    """Modal page"""

    model = Curriculum
    slug_field = "id"
    template_name = "curriculum_ms/modal.html"
    success_url = reverse_lazy("modal")
    context_object_name = "curriculum"

    def get_queryset(self):
        return self.model.objects.filter(id=self.kwargs['pk'])


def send_mailgun_email(subject, message, from_email, recipient_list):
    return requests.post(
        f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages",
        auth=("api", settings.MAILGUN_API_KEY),
        data={
            "from": settings.DEFAULT_FROM_EMAIL,
            "to": recipient_list,
            "subject": subject,
            "text": message,
        },
    )


# Add contact_view
def contact_view(request):
    """Contact page"""

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            recipient_list = ['buqlex.feedback@outlook.com']

            response = send_mailgun_email(subject, message, from_email, recipient_list)
            if response.status_code == 200:
                return redirect('success')
            else:
                print(response.json())

    else:
        form = FeedbackForm()

    return render(request, 'curriculum_ms/contact.html', {'form': form})


def success_view(request):
    return render(request, 'curriculum_ms/success.html')


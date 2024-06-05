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

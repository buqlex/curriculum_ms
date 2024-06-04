from django.urls import path

from . import views

urlpatterns = [
    # =====| HOME |=====
    path("", views.HomeView.as_view(), name="home"),

    # =====| AUTH |=====
    path("accounts/login/", views.SignInView.as_view(), name="login"),
    path("accounts/logout/", views.LogoutView.as_view(), name="logout"),

    # =====| PAGE |=====
    path("create/curriculum/", views.CreateCurriculumView.as_view(), name="create_curriculum"),
    path("list/curriculums/", views.ListCurriculumView.as_view(), name="list_curriculums"),
    path("search/curriculum/", views.SearchCurriculumView.as_view(), name="search_curriculum"),
    path("detail/<int:pk>/", views.DetailCurriculumView.as_view(), name="detail_curriculum"),
    path("edit/<int:pk>/", views.EditCurriculumView.as_view(), name="edit_curriculum"),
    # path("contact/", views.ContactView.as_view(), name="contact"),

    # =====| FORM |=====
    path("create/curriculum/new/", views.CreatedCurriculumView.as_view(), name="created_curriculum"),
    path("update/curriculum/<int:pk>/", views.UpdatedCurriculumView.as_view(), name="updated_curriculum"),
    path("modal/<int:pk>/", views.ModalView.as_view(), name="modal"),

    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]

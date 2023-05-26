from django.urls import path
from .views import (
    ApplicantSignupView,
    EmployerSignupView,
    CustomAuthToken,
    LogoutView,
    ApplicantOnlyView,
    EmployerOnlyView,
)

urlpatterns = [
    path('signup/applicant/', ApplicantSignupView.as_view(), name='applicant-signup'),
    path('signup/employer/', EmployerSignupView.as_view(), name='employer-signup'),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('applicant/page/', ApplicantOnlyView.as_view(), name='applicant-page'),
    path('employer/page/', EmployerOnlyView.as_view(), name='employer-page'),
]

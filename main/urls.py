from django.urls import path
from django.views.generic import TemplateView
from main import views

urlpatterns = [
    path(
    "contact/",
    views.ContactUsView.as_view(),
    name="contact",
    ),

    path("",
    TemplateView.as_view(template_name="home.html"),
    name="home",),

    path(
    "services/",
    TemplateView.as_view(template_name="services.html"),
    name="services",
    ),

    path(
    "design-thinking-challenge/",
    TemplateView.as_view(template_name="design-thinking-challenge.html"),
    name="design-thinking-challenge",),
]

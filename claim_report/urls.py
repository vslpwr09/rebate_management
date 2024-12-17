from django.urls import path
from .views import ClaimReport

urlpatterns = [
    path('', ClaimReport.as_view()),
]

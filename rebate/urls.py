from django.urls import path
from rebate.views import CreateRebateProgram

urlpatterns = [
    path('', CreateRebateProgram.as_view()),
]

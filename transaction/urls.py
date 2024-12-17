from django.urls import path
from .views import CreateTransaction, CalculateRabate

urlpatterns = [
    path('', CreateTransaction.as_view()),
    path('calculate-rebate/<int:transaction_id>', CalculateRabate.as_view()),

]

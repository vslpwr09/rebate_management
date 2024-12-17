from django.urls import path
from .views import ClaimRebate, UpdateClaimStatus

urlpatterns = [
    path('claim/', ClaimRebate.as_view()),
    path('update/<int:claim_id>', UpdateClaimStatus.as_view())
]

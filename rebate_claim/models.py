from django.db import models
from transaction.models import Transaction


class RebateClaim(models.Model):

    options = (
        ("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")
    )
    claim_id = models.AutoField(primary_key=True)
    transaction_id = models.ForeignKey(
        Transaction, db_column='transaction_id', on_delete=models.CASCADE,
        related_name="rebate_transaction_id"
    )
    claim_amount = models.DecimalField(max_digits=14, decimal_places=4)
    claim_status = models.CharField(max_length=10, choices=options,
                                    default=None, db_index=True)
    claim_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rebate_claim'

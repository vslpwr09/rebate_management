from django.db import models
from rebate.models import RebateProgram


class Transaction(models.Model):

    transaction_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    transaction_date = models.DateTimeField(auto_now_add=True)
    rebate_program_id = models.ForeignKey(
        RebateProgram, db_column='rebate_program_id',
        on_delete=models.CASCADE, related_name="rebate_program_id"
    )

    class Meta:
        db_table = 'transaction'

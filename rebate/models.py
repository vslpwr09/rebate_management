from django.db import models


class RebateProgram(models.Model):

    id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    rebate_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    eligibility_criteria = models.DecimalField(max_digits=14, decimal_places=4, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'rebate_program'

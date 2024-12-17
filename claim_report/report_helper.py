from rebate_claim.models import RebateClaim
from django.db.models import Sum, Count
from utils.common import Common
from django.core.cache import cache
from hashlib import md5
from datetime import timezone


class ReportHelper():
    """
    Class to do report related calculations
    """
    @staticmethod
    def generate_rebate_claim_report(report_params: dict) -> dict:
        """
        Fetch claim report related details
        Args:
            report_parat(dict): Report parameters
        Returns:
            dict: Claim report details
        """

        # Breaking up date range into serveral smaller date range
        # so that it will scan smaller part of DB table
        date_chunk = Common.split_date_range(
            start=report_params['from_date'], end=report_params['to_date'],
            chunk_size=2, format='%Y-%m-%d')  # change chunk size

        total_claims = approved_amount = 0
        for date in date_chunk:
            from_date = date[0].replace(tzinfo=timezone.utc)
            to_date = date[1].replace(tzinfo=timezone.utc)

            key_hash = md5(f'report_{from_date}_{to_date}'.encode()).hexdigest()

            # Get data from cache
            claim_data = cache.get(key_hash)

            # If cache data not found make db query
            if not claim_data:
                claim_data = RebateClaim.objects.filter(
                    claim_date__gte=from_date, claim_date__lte=to_date).annotate(
                        sum_claim_amount=Sum('claim_amount'), claim_count=Count('claim_id'))
                # Setting cache for 1 hr
                cache.set(key_hash, claim_data, timeout=3600)

            for data in claim_data:
                total_claims += data.claim_count
                if data.claim_status == 'approved':
                    approved_amount += data.sum_claim_amount

        return {"total_claims": total_claims, "approved_amount": approved_amount}

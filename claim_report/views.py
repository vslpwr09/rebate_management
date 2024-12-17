from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .validate_claim_report_rule import ValidateClaimReportRule
from .report_helper import ReportHelper


class ClaimReport(ListAPIView):
    """
    Class to generate claim report
    """
    def post(self, request):
        """
        Generate claim report
        Args:
            request(object): API input
        """
        is_failed = ValidateClaimReportRule().validate(data=request.data)

        if is_failed:
            return Response({"message": is_failed},
                            status=status.HTTP_400_BAD_REQUEST)

        report_data = ReportHelper.generate_rebate_claim_report(
            report_params=request.data)
        return Response(report_data, status=status.HTTP_200_OK)

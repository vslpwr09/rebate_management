from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from .validate_claim_rule import ValidateClaimRule
from .serializers import RebateClaimSerializer
from .models import RebateClaim


class ClaimRebate(CreateAPIView):
    """
    Create Rebate Claim class
    """
    def post(self, request):
        """
        Save a new transaction
        Args:
            request(object): Request object, API input data
        Returns:
            response(object):
        """
        # Added custom validation rules
        is_failed = ValidateClaimRule().validate(data=request.data)
        if is_failed:
            return Response({
                "message": is_failed
            }, status=status.HTTP_400_BAD_REQUEST)

        # Check if request data is valid at model level
        rebate_claim_serializer = RebateClaimSerializer(data=request.data)
        if rebate_claim_serializer.is_valid(raise_exception=True):
            rebate_claim_serializer.save(claim_status='pending')

            return Response({"message": "Claim added successfully."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": "Something went wrong."},
                            status=status.HTTP_400_BAD_REQUEST)


class UpdateClaimStatus(UpdateAPIView):
    """
    Update claim status
    """
    def put(self, request, *args, **kwargs):
        # Fetch claim id from get query param
        claim_id = kwargs['claim_id']
        claim_status = request.data['claim_status']
        error_msg = ''
        if claim_status in ['pending', 'approved', 'rejected']:
            # Fetch transaction details along with rebate program
            claim = RebateClaim.objects.filter(claim_id=claim_id).first()

            if not claim:
                error_msg = 'Invalid claim'
            elif claim and claim.claim_status in ['approved', 'rejected']:
                error_msg = f'Claim already {claim.claim_status}'

        if not error_msg:
            claim.claim_status = claim_status
            claim.save()
            return Response({"message": "Claim status updated successfully."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"message": error_msg},
                            status=status.HTTP_400_BAD_REQUEST)

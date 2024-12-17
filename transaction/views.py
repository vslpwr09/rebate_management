from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .validate_transaction_rule import ValidateTransactionRule
from .serializers import TransactionSerializer
from .models import Transaction


class CreateTransaction(CreateAPIView):
    """
    Create transaction class
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
        is_failed = ValidateTransactionRule().validate(data=request.data)
        if is_failed:
            return Response({"message": is_failed},
                            status=status.HTTP_400_BAD_REQUEST)

        transaction_serializer = TransactionSerializer(data=request.data)

        # Check if request data is valid at model level
        if transaction_serializer.is_valid():
            transaction_serializer.save()
            return Response({"message": "Transaction added successfully"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Something went wrong"},
                            status=status.HTTP_404_NOT_FOUND)


class CalculateRabate(RetrieveAPIView):
    """
    Calculate Rabate for transaction
    Args:
        request(object): Request object, API input data
        kwargs(dict): Dictionary query parameter
    Returns:
        response(object):
    """
    def get(self, request, *args, **kwargs):
        # Fetch transaction id from get query param
        transaction_id = kwargs['transaction_id']

        # Fetch transaction details along with rebate program
        transaction = Transaction.objects.select_related('rebate_program_id') \
            .filter(transaction_id=transaction_id).first()

        rebate_amount = 0
        if transaction:
            # calculate rebate amount from transaction amount
            # and rebate percentage (x * y% = a)
            if transaction.rebate_program_id.rebate_percentage > 0:
                rebate_amount = transaction.amount \
                    * (transaction.rebate_program_id.rebate_percentage / 100)

        else:
            return Response({"error": "Invalid transaction"},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({"rebate_amount": rebate_amount},
                        status=status.HTTP_200_OK)

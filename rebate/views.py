from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RebateProgramSerializer
from .validate_rebate_rule import ValidateRebateRule


class CreateRebateProgram(CreateAPIView):
    """
    Create Rebate program class
    """

    def post(self, request):
        """
        Save new Rebate program
        Args:
            request(object): Request object, API input data
        Returns:
            response(object):
        """
        # Added custom validation rules
        is_failed = ValidateRebateRule().validate(data=request.data)
        if is_failed:
            return Response({"message": is_failed},
                            status=status.HTTP_400_BAD_REQUEST)

        rebate_serializer = RebateProgramSerializer(data=request.data)

        # Check if request data is valid at model level
        if rebate_serializer.is_valid():
            rebate_serializer.save()
            return Response({"message": "Program added successfully"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Something went wrong"},
                            status=status.HTTP_400_BAD_REQUEST)

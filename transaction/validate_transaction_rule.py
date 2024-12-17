from utils.common import Common
from .models import RebateProgram
from django.utils import timezone


class ValidateTransactionRule():
    """
    Class to validate request data
    """
    def validate(self, data: dict) -> list:
        """
        Validate request data
        Args:
            data(dict): Request data
        Returns:
            error_msg(list): List of error messages
        """
        error_msg = list()

        required_fields = ['amount', 'rebate_program_id']
        missing_fields = Common.check_fields(
            required_fields=required_fields, data=data)

        if missing_fields:
            error_msg.append(self.__get_error_message(
                ', '.join(missing_fields))['missing_fields'])

        # Check if amount is valid and greater than 0
        if 'amount' in data and \
                (not isinstance(data['amount'], (int, float)) or
                    (isinstance(data['amount'], (int, float)) and
                        data['amount'] <= 0)):
            error_msg.append(
                self.__get_error_message()['invalid_amount'])

        # Return error if rebate program id is blank
        if 'rebate_program_id' in data and data['rebate_program_id'] == "":
            error_msg.append(self.__get_error_message()['blank_program_id'])

        if 'rebate_program_id' in data and data['rebate_program_id'] != "":
            program = RebateProgram.objects.\
                filter(id=data['rebate_program_id']).first()

            # Return error if the program id is not found
            if not program:
                error_msg.append(
                    self.__get_error_message()['invalid_program_id'])
            else:
                curr = timezone.now().date()
                # Return error if transaction not falling with program duration
                if not (program.start_date.date() <= curr and
                        curr <= program.end_date.date()):
                    error_msg.append(
                        self.__get_error_message()['transaction_date'])
                elif program.eligibility_criteria > data['amount']:
                    error_msg.append(
                        self.__get_error_message()['not_eligible'])

        return error_msg

    def __get_error_message(self, param='') -> dict:
        """
        Format error messages based on key and param
        Args:
            param(str): String to complete the error message
        Returns:
            dict: Dictionary of error messages
        """
        return {
            'missing_fields': f'Field(s) missing: {param}',
            'invalid_amount': 'Please enter valid amount.',
            'invalid_program_id': 'Please enter a valid Rebate program.',
            'transaction_date': 'The Rebate program is not valid for the '
            'transaction, as the transaction does not fall within the '
            'program\'s duration.',
            'blank_program_id': 'Please provide Rebate program.',
            'not_eligible': 'The transaction is not eligible for a rebate.'
        }

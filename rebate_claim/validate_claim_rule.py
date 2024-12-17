from utils.common import Common
from .models import Transaction, RebateClaim


class ValidateClaimRule():
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

        required_fields = ['transaction_id', 'claim_amount']
        missing_fields = Common.check_fields(
            required_fields=required_fields, data=data)

        if missing_fields:
            error_msg.append(self.__get_error_message(
                ', '.join(missing_fields))['missing_fields'])

        if 'transaction_id' in data and data['transaction_id'] == "":
            error_msg.append(self.__get_error_message()['blank_transaction_id'])

        if 'transaction_id' in data and data['transaction_id'] > 0:
            transaction = Transaction.objects.filter(
                transaction_id=data['transaction_id']).first()

            if not transaction:
                error_msg.append(
                    self.__get_error_message()['invalid_transaction'])

        if 'claim_amount' in data and data['claim_amount'] == "":
            error_msg.append(self.__get_error_message()['blank_claim_amount'])

        # Check if amount is either int or float
        if 'claim_amount' in data and data['claim_amount'] != "" and data['claim_amount'] <= 0:
            error_msg.append(self.__get_error_message()['invalid_claim_amount'])

        # Check if claim for the transaction is already exist
        if not error_msg:
            claim_exists = RebateClaim.objects.filter(
                transaction_id=data['transaction_id'],
                claim_amount=data['claim_amount']
            ).first()
            if claim_exists:
                error_msg.append(self.__get_error_message(
                    claim_exists.claim_status.title())['duplicate_record'])

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
            'blank_transaction_id': 'Please provide transaction.',
            'claim_amount': 'Please enter claim amount.',
            'invalid_claim_amount': 'Please enter valid claim amount.',
            'blank_claim_amount': 'Please enter claim amount.',
            'invalid_transaction': 'Invalid transaction.',
            'duplicate_record': f'You have already applied for a claim for this transaction,'
            f' and the current status of the claim is {param}.'
        }

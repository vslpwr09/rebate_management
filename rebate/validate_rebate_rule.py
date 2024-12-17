from utils.common import Common
from .models import RebateProgram


class ValidateRebateRule():
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

        required_fields = ['program_name', 'rebate_percentage',
                           'start_date', 'end_date']
        missing_fields = Common.check_fields(
            required_fields=required_fields, data=data)

        if missing_fields:
            error_msg.append(self.__get_error_message(
                ', '.join(missing_fields))['missing_fields'])

        # Check if Program name is less than 3 chars.
        if 'program_name' in data and len(data['program_name']) < 3:
            error_msg.append(self.__get_error_message()['invalid_program'])

        # Check start and end dates are valid.
        if 'start_date' in data and not Common.validate_date(
                date=data['start_date'], format='%Y-%m-%d'):
            error_msg.append(self.__get_error_message()['invalid_start_date'])

        if 'end_date' in data and not Common.validate_date(
                date=data['end_date'], format='%Y-%m-%d'):
            error_msg.append(self.__get_error_message()['invalid_end_date'])

        # Check start date is less than end date
        if not self.__get_error_message()['invalid_end_date'] in error_msg \
                and not self.__get_error_message()['invalid_start_date'] \
                in error_msg:
            diff = Common.date_diff(data['start_date'], data['end_date'])
            if diff < 0:
                error_msg.append(self.__get_error_message()['invalid_date_range'])

        # Check if the start date is a past date
        if 'start_date' in data and Common.check_past_date(
                date=data['start_date']) < 0:
            error_msg.append(self.__get_error_message()['past_date'])

        # Check if rebate percentage is valid
        if 'rebate_percentage' in data and \
                not isinstance(data['rebate_percentage'], (int, float)):
            error_msg.append(
                self.__get_error_message()['invalid_rebate_percentage'])

        # Check rebate percentage is valid and less tha 100%
        if 'rebate_percentage' in data and \
                isinstance(data['rebate_percentage'], (int, float)) \
                and data['rebate_percentage'] >= 100:
            error_msg.append(
                self.__get_error_message()['invalid_rebate_percentage'])

        # Check for duplicate entry if provided data is valid
        if not error_msg:
            program_exists = RebateProgram.objects.filter(
                program_name=data['program_name'],
                rebate_percentage=data['rebate_percentage'],
                start_date=data['start_date'],
                end_date=data['end_date']
            )
            if program_exists:
                error_msg.append(self.__get_error_message()['duplicate_record'])

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
            'invalid_program': 'Please enter valid Program Name.',
            'invalid_start_date': 'Please enter valid Start date.',
            'invalid_end_date': 'Please enter valid End date.',
            'invalid_date_range': 'Start date must be less than the end date.',
            'past_date': 'You cannot add a program for a past date.',
            'invalid_rebate_percentage': 'Please enter valid Rebate percentage.',
            'duplicate_record': 'Program alredy exists.'
        }

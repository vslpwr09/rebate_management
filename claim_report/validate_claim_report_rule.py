from utils.common import Common
from utils.constants import MAX_REPORT_DATE_RANGE


class ValidateClaimReportRule():
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

        required_fields = ['from_date', 'to_date']
        missing_fields = Common.check_fields(
            required_fields=required_fields, data=data)

        if missing_fields:
            error_msg.append(self.__get_error_message(
                ', '.join(missing_fields))['missing_fields'])

        # Check start and end dates are valid.
        if 'from_date' in data and not Common.validate_date(
                date=data['from_date'], format='%Y-%m-%d'):
            error_msg.append(self.__get_error_message()['invalid_from_date'])

        if 'to_date' in data and not Common.validate_date(
                date=data['to_date'], format='%Y-%m-%d'):
            error_msg.append(self.__get_error_message()['invalid_to_date'])

        diff = 0  # initializing diff variable
        # Check start date is less than end date
        if not self.__get_error_message()['invalid_to_date'] in error_msg and \
                not self.__get_error_message()['invalid_from_date'] in error_msg:
            diff = Common.date_diff(data['from_date'], data['to_date'])
            if diff < 0:
                error_msg.append(
                    self.__get_error_message()['invalid_date_range'])

        # Return error is selected date range is greater than max limit.
        if not error_msg:
            if diff > MAX_REPORT_DATE_RANGE:
                print(diff)
                error_msg.append(
                    self.__get_error_message(
                        MAX_REPORT_DATE_RANGE)['max_date_range'])

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
            'invalid_from_date': 'Please enter valid From date.',
            'invalid_to_date': 'Please enter valid To date.',
            'invalid_date_range': 'From date must me less than To date.',
            'max_date_range': f'Date range should be within {param} days only.'
        }

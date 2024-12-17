from datetime import datetime, timedelta


class Common:
    """
    Class contains common functions that being used across the project
    """

    @staticmethod
    def check_fields(required_fields: list, data: dict) -> list:
        """
        Get a list of missing fields from the data input.
        Args:
            required_fields(list): List of all required field
            data(dict): Data from API input
        Return:
            missing_fields(list): Returns list of missing fields
        """
        missing_fields = [fields for fields in required_fields
                          if fields not in list(data.keys())]
        return missing_fields

    @staticmethod
    def validate_date(date: str, format: str = '%Y-%m-%d') -> bool:
        """
        Check given date is valid or not
        Args:
            date(str): Date in string format
            format(str): Date format
        Return:
            bool: Return True if date is valid else False
        """
        try:
            return bool(datetime.strptime(date, format))
        except ValueError:
            return False

    @staticmethod
    def date_diff(start_date: str, end_date: str, format: str = '%Y-%m-%d') -> int:
        """
        Calculate date difference
        Args:
            start_date(str): Start date
            end_date(str): End date
        Returns:
            diff(int): No of days
        """
        diff = 0

        start = datetime.strptime(start_date, format)
        end = datetime.strptime(end_date, format)
        delta = end.date() - start.date()
        diff = delta.days
        return diff

    @staticmethod
    def check_past_date(date: str) -> int:
        """
        Check date is past date
        Args:
            date(str): Date in string format
        Returns:
            diff(int): No of days
        """
        curr = datetime.now().strftime('%Y-%m-%d')

        diff = Common.date_diff(curr, date)
        return diff

    @staticmethod
    def split_date_range(start: str, end: str, chunk_size: int, format: str) -> list:
        start_date = datetime.strptime(start, format)
        end_date = datetime.strptime(end, format)
        interval = timedelta(days=chunk_size)

        date_range = []

        period_start = start_date
        while period_start < end_date:
            period_end = min(period_start + interval, end_date)
            date_range.append((period_start, period_end))
            period_start = period_end

        return date_range

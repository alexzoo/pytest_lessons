from src.base_classes.request import Request
from configuration import BASE_URL
from src.enums.company_enums import CompanyStatuses
from src.base_classes.response import Response


class Companies:
    _COMPANIES_URL = BASE_URL + '/api/companies/'

    def get_companies(self, status=CompanyStatuses.ACTIVE.value, limit=3, offset=0):
        """
        Get company list, uses filters

        :param status: ACTIVE, BANKRUPT, CLOSED
        :param limit:
        :param offset:
        """
        params = {
            'status': status,
            'limit': limit,
            'offset': offset
        }
        request = Request(self._COMPANIES_URL).get(params=params)
        return Response(request)

    def get_company_by_id(self):
        pass

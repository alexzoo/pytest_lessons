from src.base_classes.request import Request
from configuration import BASE_URL
from src.enums.company_enums import CompanyStatuses
from src.schemas.companies import CompaniesSchema
from src.models.base_models import BaseModel


class Companies:
    _COMPANIES_URL = BASE_URL + '/api/companies/'

    def get_companies(self, status=CompanyStatuses.ACTIVE, limit=3, offset=0):
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

        return Request(self._COMPANIES_URL).get(params=params)

    def get_company_by_id(self):
        pass

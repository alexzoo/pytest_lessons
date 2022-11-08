import pytest

from src.base_classes.response import Response
from src.models.companies import Companies
from src.schemas.companies import CompaniesSchema, Meta, Data
from src.enums.company_enums import CompanyStatuses


companies = Companies()


def test_get_all_companies():
    response = companies.get_companies()

    res = Response(response)\
        .assert_status_code(200)\
        .validate(CompaniesSchema)
    print(res)


def test_get_company_with_limit():
    response = companies.get_companies(limit=2).json()
    validated_result = CompaniesSchema.parse_obj(response)
    assert validated_result.meta.limit == 2


@pytest.mark.parametrize('status, result', [
    (CompanyStatuses.ACTIVE.value, CompanyStatuses.ACTIVE.value),
    (CompanyStatuses.BANKRUPT.value, CompanyStatuses.BANKRUPT.value),
    (CompanyStatuses.CLOSED.value, CompanyStatuses.CLOSED.value),
])
def test_get_company_filter_by_status(status, result):
    response = companies.get_companies(status=status).json()
    validated_result = CompaniesSchema.parse_obj(response)

    for res in validated_result.data:
        assert res.company_status.value == result




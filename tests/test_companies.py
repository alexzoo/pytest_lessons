import pytest

from src.base_classes.response import Response
from src.models.companies import Companies
from src.schemas.companies import CompaniesSchema, Meta, Data
from src.enums.company_enums import CompanyStatuses


companies = Companies()


def test_get_all_companies():
    companies.get_companies().assert_status_code(200).validate(CompaniesSchema)


def test_get_company_with_limit():
    response = companies.get_companies(limit=2)
    validated_result = CompaniesSchema.parse_obj(response.json)
    assert validated_result.meta.limit == 2


@pytest.mark.parametrize('status, result', [
    (CompanyStatuses.ACTIVE.value, CompanyStatuses.ACTIVE.value),
    (CompanyStatuses.BANKRUPT.value, CompanyStatuses.BANKRUPT.value),
    (CompanyStatuses.CLOSED.value, CompanyStatuses.CLOSED.value),
], ids=str)
def test_get_company_filter_by_status(status, result):
    response_json = companies.get_companies(status=status).json
    validated_result = CompaniesSchema.parse_obj(response_json)

    for data in validated_result.data:
        assert data.company_status.value == result


@pytest.mark.parametrize('get_testing_scenarios', ['scenario_1'], indirect=True)
def test_get_scenarios(get_testing_scenarios):
    print(get_testing_scenarios)


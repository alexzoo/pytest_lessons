from src.base_classes.response import Response
from src.models.companies import Companies
from src.schemas.companies import CompaniesSchema


def test_get_all_companies():
    response = Companies().get_companies()
    Response(response).assert_status_code(200).validate(CompaniesSchema)



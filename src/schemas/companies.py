from pydantic import BaseModel
from src.enums.company_enums import CompanyStatuses


class DescriptionLang(BaseModel):
    translation_lang: str
    translation: str


class Data(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: CompanyStatuses
    # description: str
    # description_lang: list[DescriptionLang]


class Meta(BaseModel):
    limit: int
    offset: int
    total: int


class CompaniesSchema(BaseModel):
    data: list[Data]
    meta: Meta

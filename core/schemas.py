from pydantic import BaseModel, Field, field_validator


class BaseAmountSchema(BaseModel):
    amount: float = Field(gt=0,allow_inf_nan=False,description="Amount must be greater than zero")


class AmountCreateSchema(BaseAmountSchema):
    description: str = Field(min_length=1,max_length=200,description="Expense description")

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Description cannot be empty or whitespace")
        return value


class AmountResponsSchema(BaseAmountSchema):
    id: int = Field(gt=0)
    description: str


class AmountUpdateSchema(BaseAmountSchema):
    pass

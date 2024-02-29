from typing import Optional

from pydantic import BaseModel, EmailStr, Field, constr, conint, create_model


class SchemaDeCliente(BaseModel):
    nombre: constr(strict=True) = Field(...)
    apellido: constr(strict=True) = Field(...)
    email: EmailStr = Field(...)
    fecha_nacimiento: constr(strict=True) = Field(None)
    pais: constr(strict=True) = Field(None)
    password: constr(strict=True) = Field(None)
    class config:
        schema_extra = {
            "ejemplo": {
                "nombre": "Juana",
                "apellido": "Pilo",
                "email": "jpilo@gmail.com",
                "fecha_nacimiento": "18/12/1996",
                "pais": "Argentina",
                "password": "Clavesegura123"
            }
        }

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        fields = {
            attribute: (Optional[data_type.type_], None)
            for attribute, data_type in annonations.items()
        }
        OptionalModel = create_model(f"Optional{cls.__name__}", **fields)
        return OptionalModel


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
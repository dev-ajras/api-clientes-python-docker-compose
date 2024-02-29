from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
router = APIRouter()
from server.database import (
    add_cliente,
    delete_cliente,
    retrieve_cliente,
    retrieve_clientes,
    update_cliente,
)
from server.models.cliente import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeCliente
)

@router.post("/", response_description="Datos de cliente agregados ala base de datos")
async def add_cliente_data(cliente: SchemaDeCliente = Body(...)):
    cliente = jsonable_encoder(cliente)
    new_cliente = await add_cliente(cliente)
    return ResponseModel(new_cliente, "Cliente agregado.")


@router.get("/", response_description="Clientes retrieved")
async def get_clientes():
    clientes = await retrieve_clientes()
    if clientes:
        return ResponseModel(clientes, "Se consiguieron los datos de los clientes")
    return ResponseModel(clientes, "Vuelve una lista vacía")



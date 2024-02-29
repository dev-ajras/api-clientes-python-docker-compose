import os
import motor.motor_asyncio
from bson.objectid import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.clientes

cliente_collection = database.get_collection("clientes_collections")

# helpers

def cliente_helper(cliente) -> dict:
    return {
        "id": str(cliente["_id"]),
        "nombre": cliente["nombre"],
        "apellido": cliente["apellido"],
        "email": cliente["email"],
        "fecha_nacimiento": cliente["fecha_nacimiento"],
        "pais": cliente["pais"],
        "password": cliente["password"]
    }
    
# Buscar todes les clientes de la base de datos
async def retrieve_clientes():
    clientes = []
    async for cliente in cliente_collection.find():
        clientes.append(cliente_helper(cliente))
    return clientes

# Agregar un cliente a la base de datos

async def add_cliente(cliente_data: dict) -> dict:
    cliente = await cliente_collection.insert_one(cliente_data)
    new_cliente = await cliente_collection.find_one({"_id": cliente.inserted_id})
    return cliente_helper(new_cliente)

# Buscar un cliente a partir de un ID
async def retrieve_cliente(id: str) -> dict:
    cliente = await cliente_collection.find_one({"_id": ObjectId(id)})
    if cliente:
        return cliente_helper(cliente)


# Actulizar un cliente a partir de un ID
async def update_cliente(id: str, data: dict):
    # Devuelve falso si el cuerpo del request está vacio
    if len(data) < 1:
        return False
    cliente = await cliente_collection.find_one({"_id": ObjectId(id)})
    if cliente:
        updated_cliente = await cliente_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_cliente:
            return True
        return False

# Borrar un cliente de la base de datos
async def delete_cliente(id: str):
    cliente = await cliente_collection.find_one({"_id": ObjectId(id)})
    if cliente:
        await cliente_collection.delete_one({"_id": ObjectId(id)})
        return True
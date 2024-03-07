from fastapi import FastAPI
from server.routes.socie import router as SocieRouter
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


app.include_router(SocieRouter, tags=["Clientes"], prefix="/clientes")

@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Bienvenidos a esta fantástica aplicación"}




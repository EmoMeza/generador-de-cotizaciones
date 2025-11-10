from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

# Configuración de Mongo
mongo_url = os.getenv("mongourl", "mongodb://admin:admin123@cotizacion-db:27018")

client = AsyncIOMotorClient(mongo_url)
db = client["cotizacion"]

@app.get("/")
async def root():
    # Endpoint de prueba con MongoDB
    count = await db.collection_name.count_documents({})
    return {"message": f"FastAPI + MongoDB funcionando 🚀, documentos en la colección: {count}"}
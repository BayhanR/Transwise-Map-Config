from fastapi import FastAPI, Query
from app.services.route_service import get_route
from app.utils.logger import logger

app = FastAPI(title="TranswiseAI Rota API")

@app.get("/route")
def calculate_route(start: str = Query(...), end: str = Query(...)):
    logger.info(f"Rota isteği alındı: {start} -> {end}")
    try:
        route = get_route(start, end)
        logger.debug(f"Rota verisi: {route}")
        return route
    except Exception as e:
        logger.error(f"Rota hesaplama hatası: {str(e)}")
        return {"error": "Rota hesaplanamadı"}

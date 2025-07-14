from fastapi import FastAPI, Query
from app.services.route_planner import plan_route
from app.services.redis_client import get_route_by_id
from app.utils.logger import logger

app = FastAPI(title="TranswiseAI Rota Planlayıcı")

@app.get("/plan-route")
def plan_route_endpoint(
    pickup: str = Query(...),
    delivery: str = Query(...)
):
    try:
        response = plan_route(pickup, delivery)
        return response
    except Exception as e:
        logger.error(f"Rota planlama hatası: {str(e)}")
        return {"error": "Rota planlanamadı"}

@app.get("/route/{route_id}")
def get_route_by_id_endpoint(route_id: str):
    result = get_route_by_id(route_id)
    if result:
        return result
    return {"error": "Rota bulunamadı"}

from fastapi import FastAPI,APIRouter,Depends  
#import os 
from src.helpers.config import get_settings ,Settings

base_router=APIRouter(prefix="/api/v1",tags=["api_v1"],) 

# the decorator is >>(base_router) 
@base_router.get("/") 
async def welcome(app_settings:Settings =Depends(get_settings)):
    app_settings=get_settings()
    app_name= app_settings.APP_NAME #os.getenv("APP_NAME")
    app_version= app_settings.APP_VERSION #os.getenv("APP_VERSION") 
    return{
        "app_name":app_name,
        "app_verion":app_version,
    }
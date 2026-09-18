from fastapi import FastAPI 
from src import base
from src.routes import data 


app=FastAPI() # like a decorator  
app.include_router(base.base_router) # include the router from base.py 
app.include_router(data.data_router)


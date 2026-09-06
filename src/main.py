from fastapi import FastAPI 
from src import base



app=FastAPI() # like a decorator  
app.include_router(base.base_router) # include the router from base.py 


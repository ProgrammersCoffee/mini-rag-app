from fastapi import FastAPI 
from dotenv import load_dotenv
load_dotenv(".env") # load the environment variables from .env file

from routes import base


app=FastAPI() # like a decorator  
app.include_router(base.base_router) # include the router from base.py 


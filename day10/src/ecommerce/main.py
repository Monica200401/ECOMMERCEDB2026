from sqlalchemy import engine
 
from ecommerce.configuration.mysql_conn import base, engine

base.metadata.create_all(bind=engine)
from fastapi import fastapi
from ecommerce.controllers import customer_controller
app =FastAPI()
app.include_router(customer_controller.router)
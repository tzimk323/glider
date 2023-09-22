
from pathlib import Path
from urllib import request
from urllib.request import Request
from fastapi import FastAPI, Query, Path, HTTPException, Body,Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette import status

from starlette.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_400_BAD_REQUEST
from starlette.templating import Jinja2Templates
from fastapi import APIRouter
# from app2 import database
from .database import cars
# from .main import app2


class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(...,ge=1970,lt=2022)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]



router = APIRouter()

#...= no default value
# 10=default 10 cars
# optional=douleuei k xwris na tou dwseis noumero
# 127.0.0.1:8000/cars?number=3 an tou dwseis
# max length  3= oxi parapanw apo 999
@router.get("/carsapi",response_model=List[Dict[str,Car]])
def get_cars(number: Optional[str]= Query("10",max_length=3)):
    response = []
    for id, car in list(cars.items())[:int(number)]:
        to_add={}
        to_add[id]=car
        response.append(to_add)
    return response


# find by id
# path otan uparxei sto url otan apla mporeis na tou xwseis tin metavliti ?id tote query
@router.get("/carsapi/{id}", response_model=Car)
def get_car_by_id(id: int = Path(...,ge=0,lt=1000)):
    car = cars.get(id)
    if not car:
        # if not exist gurna not found 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Could not find car by id")
    return car

# min_id=Body oti tha mpei sto body?
# add a car with post
@router.post("/carsapi", status_code=status.HTTP_201_CREATED)
def add_cars(body_cars:List[Car],min_id: Optional[int] = Body(0)):
    if len(body_cars) < 1:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,detail="No cars to add.")
    min_id = len(cars.values()) + min_id
    for car in body_cars:
        while cars.get(min_id):
            min_id += 1
        cars[min_id] = car
        min_id += 1

#update car
@router.put("/carsapi/{id}",response_model=Dict[str,Car])
def update_car(id: int, car: Car =Body(...)):
    stored = cars.get(id)
    if not stored:
        return  HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Could not find car by id")
    stored = Car(**stored)
    # exclude everything that user didnt change
    new = car.dict(exclude_unset=True)
    new = stored.copy(update=new)
    cars[id] = jsonable_encoder(new)
    response = {}
    response[id] = cars[id]
    return response


# delete car
@router.delete("/carsapi/{id}")
def delete_car(id: int):
    if not cars.get(id):
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find car by id")
    del cars[id]

# SEE REDIRECT
@router.get("/red",response_class=RedirectResponse)
def rootredirect(request: Request):
    return RedirectResponse(url="/carsapi")
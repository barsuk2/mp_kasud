from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from enum import Enum
import redis

r = redis.Redis(host='localhost', port=6379)

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/', name='Это параметр name async', description='Это параметр description')
async def read_root():
    r.set("asd", "dsdsd")
    print(r.get("asd"))
    return {'Hello': 'egor'}


@app.get('/items/{items_id}', name='Получить элемент. Тип не проверяем')
async def read_item(items_id: int):
    r.set(items_id, f'hello world_{items_id}')
    return {'item': r.get(items_id), 'message': 'Hello world'}


@app.put('/items/{items_id}', name='Изменить элемент')
def upgrade_item(items_id: int, item: Item):
    return {'item_name': item.name, 'item_id': items_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lennet = "lennet"


@app.get('/models/{model_name}', name='Enum эксперемент')
async def enum_example(model_name: ModelName):
    print('Model ', ModelName.alexnet.value)
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW'}
    if model_name is ModelName.lennet:
        return {'model_name': model_name, 'message': 'LeCNN all the image'}
    return {'model_name': model_name, 'message': 'Have some residuals'}


@app.get('/files/')
async def getfile_path(skip: int, q: str | None = None, limit: bool = False):
    return {'file_path', skip}

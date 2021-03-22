# from enum import Enum

# from fastapi import FastAPI

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep learning FTW "}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "leCNN all the images"}
#     return { "model_name": model_name, "message": "have some residuals" }


# QUERY PARAMETER

# from typing import Optional
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#         if not short:
#             item.update(
#                 {"description": "this is amazing item that has long description"}
#                 )
#         return item

# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_user_item(
#     item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
#     ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item


# REQUEST BODY

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
        
#     return item_dict

# REQUEST BODY + query paramete +


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# app = FastAPI()


# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Optional[str] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result



# QUERY PARAMETER AND STRING VALIDATION

# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items")
# async def read_items(q: Optional[str] = Query(None, min_length=50, max_length=50)):
#     result = {"items": [{"item_id": "foo"}, {"item_id": "nasir"}]}
#     if q:
#         result.update({"q": q})
#     return result


# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")

# async def read_items(q: str = Query("fixedquery", min_length=3)):

#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# from typing import List, Optional

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: Optional[List[str]] = Query(None)):
#     query_items = {"q": q}
#     return query_items

        

# from typing import List 

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(q: List = Query([])):
#     query_items= {"q": q}
#     return query_items


# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Optional[str] = Query(None, title="Query string", min_length=3)
# ):
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#         return result

# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     q: Optional[str] = Query(
#         None,
#         title="Query string",
#         description="Query string for the items to search in the database that have good march",
#         min_length=3,
#     )
# ):
#     result = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"a": q})
#     return result



# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")

# async def read_items(

#     q: Optional[str] = Query(

#         None,
#         alias="item-query",
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#         max_length=50,
#         regex="^fixedquery$",
#         deprecated=True,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})

#     return results

# PATH PARAMETER AND NUMERIC VALIDATIONS


# from typing import Optional

# from fastapi import FastAPI, Path, Query

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(..., title="the ID of the item to get"),
#     q: Optional[str] = Query(None, alias="item=query"),
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     return result 

# from fastapi import FastAPI, Path

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: int = Path(..., title="the Id of the item to get")

# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     return result

# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(

#     q: str, item_id: int = Path(..., title="The ID of the item to get")

# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# from fastapi import FastAPI, Path, Query

# app = FastAPI()


# @app.get('/items/{item_id}')
# async def read_item(
#     *,
#     item_id: int = Path(..., title="the id of the item to get, "),
#     q: str,
#     size: float = Query(..., gt=0, lt=10.5)
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})

#     return result


# BODY MULTIPLE PARAMETER


# from typing import Optional

# from fastapi import FastAPI, Path

# from pydantic import BaseModel


# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     return result

# from typing import Optional

# from fastapi import FastAPI, Path
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results
# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="the ID of the item to get ", ge=0, le=100),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,

# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"item": item})
#     return result


# from typing import Optional

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None

# @app.put("/items/{item_id}")

# async def update_item(
#     item_id: int, 
#     item: Item, 
#     user: User, 
#     importance: int = Body(..., gt=0)
# ):
#         results = {"item_id": item_id, "item": item,"user": user, "importance": importance}
#         if q:
#             results.update({"q": a})
#         return results

# from typing import Optional

# from fastapi import Body,  FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., ebed=True)):
#     result = {"item_id": item_id, "item": item}

#     return result


# BODY FIELD

# from typing import Optional

# from fastapi import Body, FastAPI

# from pydantic import BaseModel, Field


# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: Optional[float] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     tax: Optional[float] = None
#     tag: list = []

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     result = {"item_id": item_id, "item": item}
#     return result


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[ str ] = None
#     tax: Optional[float] = None
#     tags: list = []

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     result = {"item_id": item_id, "item": item}
#     return result


# from typing import Optional

# from fastapi import FastAPI, Path
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(..., title="The ID of the item to get", ge=10, le=100),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):
#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})
#     return result



# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel


# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] =  None
#     tax: Optional[float] = None

# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     result = {"item_id": item_id, "item": item, "user": user}
#     return result
# 


#

# from typing import Optional
# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#      name: str
#      description: Optional[str] = None
#      price: float
#      tax: Optional[float] = None

# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item,  user: User, importance: int =  Body(...)
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results

# from typing import Optional

# from fastapi import Body, FastAPI

# from pydantic import BaseModel, Field


# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="The description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="The price must be greater than zero")
#     tax: Optional[float] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

# from typing import Optional

# from fastapi import Body, FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title="the description of the item", max_length=300
#     )
#     price: float = Field(..., gt=0, description="the price most be greater than zero")
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results



# from typing import Set,  Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

#     tags: Set[str] = set()



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Image(BaseModel):
#     url: str
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] =  None
#     tags: Set[str] = []
#     image: Optional[Image] =  None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     result = {"item_id": item_id, "item": item}
#     return result


# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel


# app = FastAPI()

# class Image(BaseModel):
#     url: str
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []
#     image: Optional[Image] = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results



# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


#     class Config:

#         schema_extra = {

#             "example": {

#                 "name": "Foo",

#                 "description": "A very nice Item",

#                 "price": 35.4,

#                 "tax": 3.2,

#             }

#         }



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):
#     name: str = Field(..., example="foo")
#     description: Optional[ str ] = Field(None, example="A very Nice Item")
#     price: float = Field(..., example=35.4)
#     tax: Optional[float] = Field(None, example=3.2)

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": Item}
#     return results


# from typing import Optional

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str]  = None
#     price: float
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item = Body(
#         ...,
#         example={
#             "name": "foo",
#             "description": "A very Nice Item",
#             "price": 35.5,
#             "tax": 3.5
#         }
#     )
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# from datetime import datetime, time,  timedelta
# from typing import Optional
# from uuid import UUID

# from fastapi import Body, FastAPI

# app = FastAPI()

# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: Optional[datetime] = Body(None),
#     end_datetime: Optional[datetime] = Body(None),
#     repeat_at: Optional[time] = Body(None),
#     process_after: Optional[timedelta] = Body(None),
# ):
#     start_process = start_datetime + process_after 
#     duration = end_datetime - start_process

#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#     }


# from typing import List, Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel,  EmailStr

# app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# from typing import List, Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]


# from typing import List, Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }



# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)

# async def read_item(item_id: str):
#     return items[item_id]


# from typing import List, Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5
#     tags: List[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }



# @app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)

# async def read_item(item_id: str):
#     return items[item_id]


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()



# class UserIn(BaseModel):

#     username: str

#     password: str

#     email: EmailStr
#     full_name: Optional[str] = None



# class UserOut(BaseModel):

#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None



# class UserInDB(BaseModel):

#     username: str

#     hashed_password: str

#     email: EmailStr
#     full_name: Optional[str] = None



# def fake_password_hasher(raw_password: str):

#     return "supersecret" + raw_password




# def fake_save_user(user_in: UserIn):

#     hashed_password = fake_password_hasher(user_in.password)

#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)

#     print("User saved! ..not really")
#     return user_in_db



# @app.post("/user/", response_model=UserOut)

# async def create_user(user_in: UserIn):

#     user_saved = fake_save_user(user_in)
#     return user_saved



# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class BaseItem(BaseModel):
#     description: str

# class CarItem(BaseModel):
#     type = "car"


# class PlaneItem(BaseModel):
#     type = "plane"
#     size: int




# items = {
#     "item1": {"description": "All my friend drive a low rider ", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5
#     }
# }

# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]

# from typing import Union


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()




# from typing import Optional

# from fastapi import FastAPI, Path
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")

# async def update_item(
#     *,
#     item_id: int = Path(..., title="the ID of the item to get", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):

# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Image(BaseModel):
#     url: str
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []

#     image: Optional[Image] = None



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


#     result = {"item_id": item_id}
#     if q:
#         result.update({"q": q})
#     if item:
#         result.update({"item": item})

#     return result


# from typing import List, Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = set()

#     images: Optional[List[Image]] = None



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# from typing import Optional

# from fastapi import Cookie, FastAPI

# app = FastAPI()

# @app.get("/items/")
# async def read_items(ad_id: Optional[str] = Cookie(None)):
#     return {"ad_id": ad_id}

# from typing import Optional

# from fastapi  import FastAPI, Header

# app = FastAPI()

# @app.get("/items/")
# async def read_items(user_agent: Optional[str] = Header(None)):
#     return {"User-Agent": user_agent}

# from typing import Optional

# from fastapi import FastAPI, Header

# app = FastAPI()


# @app.get("/items/")
# async def read_items(

#     strange_header: Optional[str] = Header(None, convert_underscores=False)

# ):
#     return {"strange_header": strange_header}


# from typing import List, Optional

# from fastapi import FastAPI, Header

# app = FastAPI()


# @app.get("/items/")

# async def read_items(x_token: Optional[List[str]] = Header(None)):

#     return {"X-Token values": x_token}

# from typing import List, Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] =None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     return item

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None

# # Done do this in production!

# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None

# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: float = 10.5


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }


# @app.get(
#     "/items/{item_id}/name",
#     response_model=Item,

#     response_model_include={"name", "description"},

# )
# async def read_item_name(item_id: str):
#     return items[item_id]



# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})

# async def read_item_public_data(item_id: str):
#     return items[item_id]


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr


# app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserInDB(BaseModel):
#     Username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password

# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User saved! ..not realy")
#     return user_in_db


# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved  






# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()



# class UserIn(BaseModel):

#     username: str

#     password: str

#     email: EmailStr
#     full_name: Optional[str] = None



# class UserOut(BaseModel):

#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None



# class UserInDB(BaseModel):

#     username: str

#     hashed_password: str

#     email: EmailStr
#     full_name: Optional[str] = None



# def fake_password_hasher(raw_password: str):

#     return "supersecret" + raw_password




# def fake_save_user(user_in: UserIn):

#     hashed_password = fake_password_hasher(user_in.password)

#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)

#     print("User saved! ..not really")
#     return user_in_db



# @app.post("/user/", response_model=UserOut)

# async def create_user(user_in: UserIn):

#     user_saved = fake_save_user(user_in)
#     return user_saved


# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()



# class UserBase(BaseModel):

#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None



# class UserIn(UserBase):

#     password: str




# class UserOut(UserBase):

#     pass




# class UserInDB(UserBase):

#     hashed_password: str



# def fake_password_hasher(raw_password: str):
#     return "supersecret" + raw_password


# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print("User saved! ..not really")
#     return user_in_db


# @app.post("/user/", response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved


# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app  = FastAPI()



# class CarItem(BaseItem):
#     type = 'Car'


# class PlaneItem(BaseItem):
#     type: "plane"
#     size: int




# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }

# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]


# from fastapi import FastAPI, Form


# app = FastAPI()


# @app.post("/login/")
# async def login(username: str = Form(...), password: str = Form(...)):
#     return {"username": username}



# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()

# @app.post("/files")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}

# @app.post("/uploadfile/")
# async def creat_upload_file(file: UploadFile = File(...)):
#     return {"filename": file.filename}


# from typing import List

# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import HTMLResponse

# app = FastAPI()


# @app.post("/files/")

# async def create_files(files: List[bytes] = File(...)):

#     return {"file_sizes": [len(file) for file in files]}


# @app.post("/uploadfiles/")

# async def create_upload_files(files: List[UploadFile] = File(...)):

#     return {"filenames": [file.filename for file in files]}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)


# from fastapi import FastAPI, File, Form, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(
#     file: bytes = File(...), fileb: UploadFile = File(...), token: str = Form(...)
# ):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "fileb_content_type": fileb.content_type,
#     }


# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {"foo": "the foo wrestlers"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="item not found")
#     return {"item": item[item_id]}

# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {"foo": "the foo wrestlers"}

# @app.get("/items-header/{item_id}")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",
#             headers={"X-Error": :"there goes my error"},
#         )
#     return {"item": item[item_id]}

# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# items = {"foo": "The Foo Wrestlers"}


# @app.get("/items-header/{item_id}")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=404,
#             detail="Item not found",

#             headers={"X-Error": "There goes my error"},

#         )
#     return {"item": items[item_id]}




# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse



# class UnicornException(Exception):

#     def __init__(self, name: str):

#         self.name = name



# app = FastAPI()



# @app.exception_handler(UnicornException)

# async def unicorn_exception_handler(request: Request, exc: UnicornException):

#     return JSONResponse(

#         status_code=418,

#         content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},

#     )



# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":

#         raise UnicornException(name=name)

#     return {"unicorn_name": name}



# from fastapi import FastAPI, HTTPException
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import PlainTextResponse
# from starlette.exceptions import HTTPException as StarletteHTTPException

# app = FastAPI()

# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail),  status_code=exc.status_code)



# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     return PlainTextResponse(str(exc), status_code=400)

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418,  detail="Nope! dont like 3 ")
#     return {"item_id": item_id}


# from fastapi import FastAPI, Request, status
# from fastapi.encoders import jsonable_encoder
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel

# app = FastAPI()

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )

# class Item(BaseModel):
#     title: str
#     size: int

# @app.post("/items/")
# async def create_item(item: Item):
#     return item


# from fastapi import FastAPI, HTTPException

# from fastapi.exception_handlers import (
#     http_exception_handler,
#     request_validation_exception_handler,
# )

# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException as StarletteHTTPException

# app = FastAPI()

# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request,  exc):
#     print(f"OMG! An HTTP error: {repr(exc)}")
#     return await http_exception_handler(request, exc)

# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request, exc):
#     print(f"OMG! the client send invalid data!: {exc}")
#     return await request_validation_exception_handler(request, exc)

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     if item_id == 3:
#         raise HTTPException(status_code=418, detail="Nope! i realy love 3")
#     return {"item_id": item_id}

# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []

# # @app.post("/items/", response_model=Item,  tags=["items"])
# # async def create_item(item: Item):
# #     return item

# # @app.get("/items/", tags=["items"])
# # async def read_item():
# #     return [{"name": "foo", "price": 42}]

# # @app.get("/items/", tags=["users"])
# # async def read_users():
# #     return [{"username": "johndoe"}]


# @app.post("/items/", response_model=Item, tags=["items"])
# async def create_item(item: Item):
#     return item


# @app.get("/items/", tags=["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]


# @app.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "johndoe"}]


# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []

# @app.post(
#     "/items/",
#     response_model=Item,
#     summary="Create an item",
#     description="Create an item with all the information, name, description, price, tags and set of unique tags "
# )
# async def create_item(item: Item):
#     return item


# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []


# @app.post("/items/", response_model=Item, summary="Create an item")
# async def create_item(item: Item):

#     """

#     Create an item with all the information:



#     - **name**: each item must have a name

#     - **description**: a long description

#     - **price**: required

#     - **tax**: if the item doesn't have tax, you can omit this

#     - **tags**: a set of unique tag strings for this item

#     """

#     return item


# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []


# @app.post(
#     "/items/",
#     response_model=Item,
#     summary="Create an item",

#     response_description="The created item",

# )
# async def create_item(item: Item):
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item

# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []


# @app.post(
#     "/items/",
#     response_model=Item,
#     summary="Create an item",

#     response_description="The created item",

# )
# async def create_item(item: Item):
#     """
#     Create an item with all the information:

#     - **name**: each item must have a name
#     - **description**: a long description
#     - **price**: required
#     - **tax**: if the item doesn't have tax, you can omit this
#     - **tags**: a set of unique tag strings for this item
#     """
#     return item


# from datetime import datetime
# from typing import Optional

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# fake_db = {}

# class Item(BaseModel):
#     title: str
#     timestamp: datetime
#     description: Optional[str] = None

# app = FastAPI()

# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#     json_compatible_item_date = jsonable_encoder(item)
#     fake_db[id] =json_compatible_item_date


# from typing import List, Optional

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     tax: float = 10.5
#     tags: List[str] = []



# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

# @app.get("items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]


# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     update_item_encoded = jsonable_encoder(item)
#     item[item_id] = update_item_encoded
#     return update_item_encoded


# from typing import List, Optional

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     tax: float = 10.5
#     tags: List[str] = []

# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.patch("items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     stored_item_data = items[item_id]
#     stored_item_model = Item(**stored_item_data)
#     update_data = item.dict(exclude_unset=True)
#     update_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(update_item)
#     return update_item


# from typing import Optional, List

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     tax: float = 10.5
#     tags: List[str] = []





# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }

# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.patch("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     stored

# from typing import Optional 

# from fastapi import Depends, FastAPI

# app = FastAPI()

# async def common_parameter(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}

# @app.get("/items/")
# async def read_item(commons: dict = Depends(common_parameter)):
#     return commons

# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameter)):
#     return commons

# from typing import Optional

# from fastapi import Depends, FastAPI

# app = FastAPI()

# async def common_parameter(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameter)):
#     return commons


# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameter)):
#     return commons

# from typing import Optional

# from fastapi import Depends, FastAPI

# app = FastAPI()

# fake_items_db = [{"item_name": "foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]



# class CommonQueryParams:
#     def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
#         self.q = q
#         self.skip = skip
#         self.limit = limit

# @app.get("/items/")
# async def read_items(commons: CommonQueryParams = Depends()):
#     response = {}
#     if commons.q:
#         response.update({"q": commons.q})
#     items = fake_items_db[commons.skip : commons.skip + commons.limit]
#     response.update({"items": items})
#     return response



# from typing import Optional

# from fastapi import Cookie, Depends,  FastAPI

# app = FastAPI()

# def query_extractor(q: Optional[str] = None):
#     return q

# def query_or_cokies_extractor(
#     q: str = Depends(query_extractor), last_query: Optional[str] = Cookie=(None)
# ):
#     if not q:
#         return last_query
#     return q

# @app.get("/items/")
# async def read_query(query_or_default: str = Depends(query_or_cokies_extractor)):
#     return {"q_or_cokies": query_or_default}

# from typing import Optional

# from fastapi import Cookie, Depends, FastAPI

# app = FastAPI()



# def query_extractor(q: Optional[str] = None):

#     return q



# def query_or_cookie_extractor(
#     q: str = Depends(query_extractor), last_query: Optional[str] = Cookie(None)
# ):
#     if not q:
#         return last_query
#     return q


# @app.get("/items/")
# async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
#     return {"q_or_cookie": query_or_default}


# from fastapi import Depends, FastAPI, Header, HTTPException

# app = FastAPI()

# async def verify_token(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token Header Invalid")
#     # return x_token

# async def verify_key(x_key: str = Header(...)):
#     if x_key != "fake-super-secret-key":
#         raise HTTPException(status_code=400, detail="X-Key Header Invalid")
#     return x_key


# @app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
# async def read_items():
#     return [{"item": "foo"}, {"item": "Bar"}]


# from fastapi import Depends, FastAPI, Header,  HTTPException

# async def verify_token(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400,  detail="X-token Header Invalid")

# async def verify_key(x_key: str = Header(...)):
#     if x_key != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token Header Invalid")
#     return x_key

# app =  FastAPI(dependencies=[Depends(verify_token),  Depends(verify_key)])

# @app.get("/items/")
# async def read_items():
#     return [{"item": "Portal Gun"}, {"item": "Plumbus"}]


# @app.get("/users/")
# async def read_users():
#     return [{"username": "Rick"}, {"username:": "Morty"}]
    
# from fastapi import Depends



# async def dependency_a():

#     dep_a = generate_dep_a()
#     try:
#         yield dep_a
#     finally:
#         dep_a.close()



# async def dependency_b(dep_a=Depends(dependency_a)):

#     dep_b = generate_dep_b()
#     try:
#         yield dep_b
#     finally:
#         dep_b.close(dep_a)



# async def dependency_c(dep_b=Depends(dependency_b)):

#     dep_c = generate_dep_c()
#     try:
#         yield dep_c
#     finally:
#         dep_c.close(dep_b)

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/items/")
# async def read_item(token: str = Depends(oauth2_schema)):
#     return {"token": token}

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}


# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/item/")
# async def read_items(token: str = Depends(oauth2_schema)):
#     return {"token": token}


# from typing import Optional

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel


# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")


# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None


# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="nasirabba@gmail.com", full_name = "Nasir Ibrahim Abba"
#     )


# async def get_curren_user(token: str = Depends(oauth2_schema)):
#     user  = fake_decode_token(token)
#     return user

# @app.get("/users/me")
# async def read_user_me(current_user: User = Depends(get_curren_user)):
#     return current_user


# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_schema)):
#     return {"token": token}



# from typing import Optional

# from fastapi import Depends, FastAPI

# from fastapi.security import OAuth2PasswordBearer
# from pydantic import BaseModel


# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# class User(BaseModel):
#     username: str
#     emai: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None

# def fake_decode_token(token):
#     return User(
#         username=token + "fakedecoded", email="ibrahimnasir618@gmail.com", full_name="Nasir Ibrahim Abba"
#     )

# async def get_curren_user(token: str = Depends(oauth2_schema)):
#     user  = fake_decode_token(token)
#     return user

# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_curren_user)):
#     return current_user


# from typing import Optional

# from fastapi import Depends, FastAPI,  HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from pydantic import BaseModel

# fake_user_db = {
#     "Nasir": {
#         "username": "Nasir",
#         "full_name": "Ibrahim Nasir Abba",
#         "email": "ibrahimnasir618@gmail.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "alice Wonderson",
#         "email": "aliewonderson@gmail.com",
#         "hashed_password": "fakehashedpassword",
#         "disaled": True
#     }
# }


# app = FastAPI()

# def fake_hashed_password(password: str):
#     return "fakehashed" + password


# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")



# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None


# class UserInDB(User):
#     hashed_password: str

# def get_user(db,  username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)


# def fake_decode_token(token):
#     # this doesn't provide security at all
#     # check the next version
#     user = get_user(fake_user_db, token)
#     return user

# async def get_current_user(token: str = Depends(oauth2_schema)):
#     user = fake_decode_token(token)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invlid authentication credential",
#             headers={"WWW=Authenticate": "Bearer"},
#         )
#     return user



# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# @app.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user_dict = fake_users_db.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(status=400,  detail="Incorect username or password")
#     user = UserInDB(**user_dict)
#     hashed_password = fake_hashed_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(status_code=400, detail="Incorect username or passwor")
#     return {"access_token": user.username, "token_type": "bearer"}

# @app.get("/users/me")
# async def read_user_me(current_user: User = Depends(get_curren_active_user)):
#     return current_user


#  Json TOKEN SECURITY

# from datetime import datetime, timedelta
# from typing import Optional

# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWTError, jwt

# from passlib.context import CryptContext

# from pydantic import BaseModel

# # to get a string like this run:
# # openssl rand -hex 32
# SECRET_KEY = "e34db00beaf5613d1e480abeb86026f543d58a8d02821887b8626aae453400f1"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30


# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: Optional[str] = None


# class User(BaseModel):
#     username: str
#     email: Optional[str] = None
#     full_name: Optional[str] = None
#     disabled: Optional[bool] = None


# class UserInDB(User):
#     hashed_password: str



# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# app = FastAPI()



# def verify_password(plain_password, hashed_password):

#     return pwd_context.verify(plain_password, hashed_password)




# def get_password_hash(password):

#     return pwd_context.hash(password)



# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)



# def authenticate_user(fake_db, username: str, password: str):

#     user = get_user(fake_db, username)

#     if not user:

#         return False

#     if not verify_password(password, user.hashed_password):

#         return False

#     return user



# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user(fake_users_db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.get("/users/me/", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


# @app.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]




# CORS MIDLLWARE


from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [

    "http://localhost.tiangolo.com",

    "https://localhost.tiangolo.com",

    "http://localhost",

    "http://localhost:8080",

]



app.add_middleware(

    CORSMiddleware,

    allow_origins=origins,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)



@app.get("/")
async def main():
    return {"message": "Hello World"}

from fastapi import FastAPI 
from fastapi import *
from pydantic import *
from model import Item
#initializing fatsapi
app = FastAPI()



inventory = {
    1:{
    "name":"Milk",
    "price":3,
    "brand" : "Regular"
    },
    2:{
    "name":"Soda",
    "price":30,
    "brand" : "Ben"
    }
}

#getting  all inventory
@app.get("/items")
def getAll():
 return inventory

@app.get("/item/{itemId}")
def getItem(itemId:int):
 return inventory[itemId]


@app.post("/new/item/{id}")
def createItem(item:Item ,  id:int):
 if id in inventory:
  return "Item already exist"
 else:
  inventory[id] = item
  return {"data" : inventory}

@app.put("/update/{id}")
def updateItem(id:int ,  item:Item):
 if id in inventory :
  inventory[id].update(item)
  return {"updated" : inventory[id]}
 else: return "Do not exist"
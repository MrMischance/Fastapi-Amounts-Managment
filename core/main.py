from fastapi import FastAPI, HTTPException, status
import random
from typing import Optional
from schemas import AmountCreateSchema, AmountResponsSchema, AmountUpdateSchema
from typing import List

app = FastAPI()

amount_list = [
    {"id":1,"description":"کتاب","amount":12000},
    {"id":2,"description":"شلوار","amount":16000},
    {"id":3,"description":"لباس","amount":18000}
]



@app.get("/amounts", response_model= List[AmountResponsSchema])
def amount_name(search: Optional[str] = None):
    if search:
        filtered_names = [name for name in amount_list if search.lower() in name["name"].lower()]
        return filtered_names
    return amount_list


@app.get("/amounts/{amount_id}", response_model=AmountResponsSchema)
def amount_detail(amount_id: int):
    for item in amount_list:
        if item["id"] == amount_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")


@app.post("/amounts",status_code=status.HTTP_201_CREATED, response_model=AmountResponsSchema)
def amount_create(items : AmountCreateSchema):
    while True:
        x = random.randint(3,100)
        for item in amount_list:
            if x != item["id"]:
                new_amount = {"id": x,"description": items.description, "amount": items.amount}
                amount_list.append(new_amount)
                return new_amount
            break


@app.put("/amounts/{amount_id}",status_code=status.HTTP_200_OK,response_model=AmountResponsSchema)
def amounts_update(amount_id: int, items: AmountUpdateSchema):
    for n in amount_list:
        if n["id"] == amount_id:
            n["amount"] = items.amount
            return n
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Amount not found")


@app.delete("/amoutns/{amount_id}", status_code=status.HTTP_204_NO_CONTENT)
def amounts_delete(amount_id: int):
    for n in amount_list:
        if n["id"] == amount_id:
            amount_list.remove(n)
            return {"message": f"Name with ID {amount_id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")


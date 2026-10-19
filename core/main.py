from fastapi import FastAPI, HTTPException, status
import random
from typing import Optional

app = FastAPI()

amount_list = [
    {"id":1,"description":"کتاب","amount":12000},
    {"id":2,"description":"شلوار","amount":16000},
    {"id":3,"description":"لباس","amount":18000}
]



@app.get("/amounts")
def amount_name(search: Optional[str] = None):
    if search:
        filtered_names = [name for name in amount_list if search.lower() in name["name"].lower()]
        return filtered_names
    return amount_list


@app.get("/amounts/{amount_id}")
def amount_detail(amount_id: int):
    for item in amount_list:
        if item["id"] == amount_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")


@app.post("/amounts",status_code=status.HTTP_201_CREATED)
def amount_create(description: str,amount: float):
    while True:
        x = random.randint(3,100)
        for item in amount_list:
            if x != item["id"]:
                new_amount = {"id": x,"description": description, "amount": amount}
                amount_list.append(new_amount)
                return new_amount
            break


@app.put("/amounts/{amount_id}",status_code=status.HTTP_200_OK)
def amounts_update(amount_id: int,description: str, amount: float):
    for n in amount_list:
        if n["id"] == amount_id and n["description"] == description:
            n["amount"] = amount
            return {"message": f"Name with ID {amount_id} updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")


@app.delete("/amoutns/{amount_id}", status_code=status.HTTP_204_NO_CONTENT)
def amounts_delete(amount_id: int):
    for n in amount_list:
        if n["id"] == amount_id:
            amount_list.remove(n)
            return {"message": f"Name with ID {amount_id} deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Name not found")


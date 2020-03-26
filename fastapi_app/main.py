import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from db.dal import async_customer_actions
from api.models import responses

app = FastAPI()

cache = {}
USE_CACHE = False


@app.get("/customer/{customer_id}", response_model=responses.Customer)
async def get_customer(customer_id: int):
    try:
        if USE_CACHE and customer_id in cache:
            return cache.get(customer_id)

        db_customer = await async_customer_actions.get_last_customer()
        res_customer = responses.Customer(**db_customer.to_dict())
        cache[customer_id] = res_customer
        return res_customer
    except Exception as e:
        print(e)
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Customer not Found!"})


@app.post("/customer", response_model=responses.Customer)
async def customer(cust: responses.Customer):
    print(f"got new customer for creation: {cust}")
    try:
        db_customer = await async_customer_actions.create_customer(name=cust.name, domain=cust.domain, is_active=True)
        res_customer = responses.Customer(**db_customer.to_dict())
        return res_customer
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": e})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5002, loop='uvloop', workers=1)
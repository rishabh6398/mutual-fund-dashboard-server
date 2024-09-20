from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth import oauth2_scheme

router = APIRouter()

# Define a request model for the purchase
class PurchaseRequest(BaseModel):
    scheme_code: int
    amount: float

@router.post("/purchase")
async def purchase_units(purchase_request: PurchaseRequest, token: str = Depends(oauth2_scheme)):
    # Logic to handle purchase request
    return {"message": "Purchase request received", "scheme_code": purchase_request.scheme_code, "amount": purchase_request.amount}

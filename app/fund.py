from fastapi import APIRouter, Depends, HTTPException
import httpx
from .auth import get_current_user
from .config import RAPIDAPI_KEY, RAPIDAPI_HOST, RAPIDAPI_URL

router = APIRouter()

@router.get("/fund-families")
async def get_fund_families():
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST,
        'Content-Type': 'application/json'
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(RAPIDAPI_URL, headers=headers)
        if response.status_code == 200:
            schemes = response.json()
            fund_families = {scheme['Mutual_Fund_Family'] for scheme in schemes}
            return list(fund_families)
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch fund data")

@router.get("/schemes/{fund_family}")
async def get_open_ended_schemes(fund_family: str, token: str = Depends(get_current_user)):
    headers = {
        'x-rapidapi-key': RAPIDAPI_KEY,
        'x-rapidapi-host': RAPIDAPI_HOST,
        'Content-Type': 'application/json'
    }
    params = {
        "Scheme_Type": "Open Ended Schemes",
        "Mutual_Fund_Family": fund_family
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(RAPIDAPI_URL, params=params, headers=headers)
        if response.status_code == 200:
            schemes = response.json()
            open_ended_schemes = [
                {
                    "scheme_code": scheme['Scheme_Code'],
                    "scheme_name": scheme['Scheme_Name'],
                    "nav": scheme['Net_Asset_Value'],
                    "date": scheme['Date'],
                    "scheme_type": scheme['Scheme_Type']
                }
                for scheme in schemes if scheme['Scheme_Type'] == "Open Ended Schemes"
            ]
            return open_ended_schemes
        else:
            raise HTTPException(status_code=response.status_code, detail="Failed to fetch scheme data")

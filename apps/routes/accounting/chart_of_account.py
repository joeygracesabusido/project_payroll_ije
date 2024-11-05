from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from pydantic import BaseModel
#from bson import ObjectId


#from pymongo import  DESCENDING


from datetime import datetime, timedelta, date
from apps.authentication.authenticate_user import get_current_user
from apps.base_model.chart_of_account_bm import ChartofAccountBM
from apps.views.accounting.chart_of_account_views import ChartofAccountViews



api_chart_of_account = APIRouter()
templates = Jinja2Templates(directory="apps/templates")


@api_chart_of_account.post('/api-insert-chart-of-account/')
async def insert_chart_of_account(items:ChartofAccountBM, username: str = Depends(get_current_user)):

    
    try:
        ChartofAccountViews.insert_chart_of_account(items,username)
        return {"message": "Account type added successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# @api_chart_of_account.post('/api-get-chart-of-account/')
# async def get_chart_of_accout_api(items:ChartofAccountBM, username: str = Depends(get_current_user)):

    
#     try:
#         ChartofAccountViews.insert_chart_of_account(items,username)
#         return {"message": "Account type added successfully"}
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@api_chart_of_account.get('/api-get-chart-of-accounts/', response_model=List[ChartofAccountBM])
async def get_chart_of_accounts(username: str = Depends(get_current_user)):
    try:
        # Call the method to get the list of chart of accounts
        chart_of_accounts = ChartofAccountViews.get_chart_of_account()
        
        if chart_of_accounts is None:
            raise HTTPException(status_code=404, detail="No chart of accounts found")
        
        return chart_of_accounts

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
# response_model=List[dict]
@api_chart_of_account.get("/api-autocomplete-chart-of-account/")
async def autocomplete_chart_of_account(term: Optional[str] = None, username: str = Depends(get_current_user)):
    try:
        # Retrieve all chart of account data from the database
        chart_of_accounts = ChartofAccountViews.get_chart_of_account()
        
        # Filter chart of accounts based on the search term
        if term:
            filtered_coa = [
                item for item in chart_of_accounts
                if term.lower() in item.chart_of_account.lower()
            ]
        else:
            filtered_coa = chart_of_accounts  # If no term is provided, return all

        # Construct suggestions from filtered chart of account data
        suggestions = [
            {
                "value": f"{item.chart_of_account}",
                "id": item.id,
                "chart_of_account_code": item.chart_of_account_code,
                "description": item.description,
                "account_type_id": item.accoun_type_id,
                "user": item.user,
                "date_created": item.date_created,
                "date_updated": item.date_updated
            }
            for item in filtered_coa
        ]

        return suggestions

    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)
    
    



  





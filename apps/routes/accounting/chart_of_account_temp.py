from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel



#from bson import ObjectId

from ...authentication.authenticate_user import get_current_user

api_chart_of_account_temp= APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")


@api_chart_of_account_temp.get("/api-chart-of-account-temp/", response_class=HTMLResponse)
async def api_chart_of_account_template(request: Request,username: str = Depends(get_current_user)):
    return templates.TemplateResponse("accounting/chart_of_account.html", {"request": request})


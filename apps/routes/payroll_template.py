from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel

#from  ..database.mongodb import create_mongo_client
#mydb = create_mongo_client()

#from bson import ObjectId

from  ..authentication.authenticate_user import get_current_user

api_payroll_temp= APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")


@api_payroll_temp.get("/api-payroll-temp/", response_class=HTMLResponse)
async def api_ticketing(request: Request,username: str = Depends(get_current_user)):
    return templates.TemplateResponse("payroll/add_employee.html", {"request": request})

@api_payroll_temp.get("/api-update-employee-temp/{id}", response_class=HTMLResponse)
async def api_update_inventory_html(id: str, request: Request, username: str = Depends(get_current_user)):

    try:
        if username == 'joeysabusido' or username == 'Dy':
            # Convert id to ObjectId
            obj_id = ObjectId(id)

            # Query for the specific inventory item
            items = mydb.employee_list.find_one({'_id': obj_id})
            
            if items:
                # Convert ObjectId to string and prepare data for template
                employee_list_data = {
                   "id": str(items['_id']),   
                    "company": items['company'],
                    "department": items['department'],
                    "employee_no": items['employee_no'],
                    "first_name": items['first_name'],
                    "last_name": items['last_name'],
                    "designation": items['designation'],
                    "salary_status": items['salary_status'],
                    "rate": items['rate'],
                    "salary_status": items['salary_status'],
                    "employee_status": items['employee_status'],
                    "user": items['user'],
                    "date_created": items['date_created'],
                    "date_updated": items['date_updated'],
                }
                 


               
                return templates.TemplateResponse("payroll/update_employee.html", {"request": request,"employee_list_data":employee_list_data })
            else:
                # Handle case where item with given id is not found (optional)
                return JSONResponse(status_code=404, content={"message": "Employee item not found"})
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authorized",
            # headers={"WWW-Authenticate": "Basic"},
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@api_payroll_temp.get("/api-payroll-computation/", response_class=HTMLResponse)
async def api_payroll_comp(request: Request,username: str = Depends(get_current_user)):
    return templates.TemplateResponse("payroll/payroll_comp.html", {"request": request})

@api_payroll_temp.get("/api-payroll-comp2/", response_class=HTMLResponse)
async def api_payroll_comp2(request: Request,username: str = Depends(get_current_user)):
    return templates.TemplateResponse("payroll/payroll_comp2.html", {"request": request})


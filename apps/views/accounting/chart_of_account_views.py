from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from apps.models.accounting.chart_of_account import ChartofAccount
from apps.database.databases import connectionDB
from typing import Optional
from datetime import date, datetime


from apps.base_model.chart_of_account_bm import ChartofAccountBM

engine = connectionDB.conn()


class ChartofAccountViews(): # this class is for Type of Account

    @staticmethod
    def insert_chart_of_account(item: ChartofAccountBM,username: str): # this is for inserting type of Account 
        
         # Create a dictionary from the item
        item_data = item.dict()  # Assuming item is a Pydantic model
        item_data['user'] = username  # Insert the username
        
        # Create an instance of AccountType using ** unpacking
        insertData = ChartofAccount(**item_data)
        

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()

    @staticmethod
    def get_chart_of_account(): # this function is to get a list of type of account
        with Session(engine) as session:
            try:
                statement = select(ChartofAccount).order_by(ChartofAccount.chart_of_account_code)

             
                results = session.exec(statement) 

                data = results.all()
                
                return data
            except :
                return None
            
    # @staticmethod
    # def update_account_type(account_type_id: int, new_account_type: str):
    #     """This function updates the account type in the database"""
        
    #     with Session(engine) as session:
    #         try:
    #             # Find the record to update
    #             statement = select(AccountType).where(AccountType.id == account_type_id)
    #             result = session.exec(statement).one_or_none()
                
    #             if result:
    #                 # Update the record's account_type
    #                 result.account_type = new_account_type
                    
    #                 # Commit the changes
    #                 session.add(result)
    #                 session.commit()
                    
    #                 # Optionally refresh the instance
    #                 session.refresh(result)
    #                 return True  # Update was successful
    #             else:
    #                 return False  # Record not found
    #         except Exception as e:
    #             # Handle any exceptions that occur
    #             print(f"An error occurred: {e}")
    #             return None
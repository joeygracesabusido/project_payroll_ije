from typing import Optional,List
from pydantic import condecimal
from sqlmodel import Field, Session, SQLModel, create_engine,select,func,funcfilter,within_group,Relationship

from datetime import datetime, date


import urllib.parse


class connectionDB:

    def conn():
        
        connection_string = "mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(
            user="joeysabusido",
            password=urllib.parse.quote("Genesis@11"),
            host="192.46.225.247",
            port=3306,
            database="project_jhoy"
        )


        engine = create_engine(connection_string, echo=True)
        return engine
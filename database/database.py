import os
from peewee import SqliteDatabase, PostgresqlDatabase
from dotenv import load_dotenv

load_dotenv()

# db = SqliteDatabase('customermanager.db')
db = PostgresqlDatabase(os.getenv('DATABASE_URI',''))

# test_db_connection.py
from sqlalchemy import create_engine

# Replace with your actual MySQL credentials
user = 'root'
password = 'Austin78702!'
host = 'localhost'
port = '3306'
database = 'ecommerce_api'

# Build connection string
connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'

try:
    engine = create_engine(connection_string)
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
except Exception as e:
    print("Failed to connect to database:")
    print(e)

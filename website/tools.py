from asyncio import exceptions
import sqlite3
import string
import secrets

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("website/database/orders.db")
    except Exception as e:
        print(e)
    return connection

def generator_id():
    alphabet = string.ascii_letters + string.digits
    id = "".join(secrets.choice(alphabet)for i in range(7))
    return id

def price(pencil: float, binder: float, pen: float,)->float :
    total_price = 0
    pencil_price = 4
    binder_price = 3.2
    pen_price = 2.7
    total_price = (pencil_price * pencil ) + (binder_price * binder) + (pen_price * pen)
    return total_price
    

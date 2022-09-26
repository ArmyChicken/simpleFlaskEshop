from pydoc import render_doc
from website import tools 
import sqlite3
from website import create_app
from flask import Flask, render_template,redirect, url_for, request, session

app=create_app()

@app.route("/", methods=["GET", "POST"])
def home():
    
    return render_template("/home.html")

@app.route("/processOrder", methods=["POST"])
def processOrder():
    session["quantityPencil"] = request.form.get("pencil")
    session["quantityBinder"]  = request.form.get("binder")
    session["quantityPen"]  = request.form.get("pen")
    return redirect(url_for('buyPage'))

@app.route("/buyPage", methods=["GET", "POST"])
def buyPage():
        quantityPencil = session["quantityPencil"]
        quantityBinder = session["quantityBinder"]
        quantityPen = session["quantityPen"]
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        total_price = tools.price(quantityBinder, quantityPen, quantityPencil)
        orderId = tools.generator_id()
        connection = tools.create_connection()
        cur = connection.cursor()
        sql_string = ("INSERT INTO tabulkos (price, pen, pencil, binder, ID, email, name, lastName, processed) VALUES (?,?,?,?,?,?,?,?,?)")
        parametry = (total_price, quantityPen, quantityPencil, quantityBinder, orderId, email, lastName, firstName, 0 )
        cur.execute(sql_string, parametry)
        return render_template("/buyPage.html")

if __name__ == "__main__":
    app.run(debug=True)
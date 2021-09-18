from utils import *
from flask import Flask, request
import json

# Responses
# Function to return success response
def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

# Function to return failure response
def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

# Creating flask server
app = Flask(__name__)  

# Send money
@app.route("/send", methods=["POST"])
def sendAPI():
    body = json.loads(request.data)
    email = str(body["email"])
    firstname = str(body["firstname"])
    lastname = str(body["lastname"])
    businessname = str(body["businessname"])
    countrycode = str(body["countrycode"])
    phoneCountryCode = str(body["phoneCountryCode"])
    phone = str(body["phone"])
    amount = int(body["amount"])

    res = sendMoney(email, firstname, lastname, businessname, countrycode, phoneCountryCode, phone, amount)

    if res == None:
      return failure_response("Something went wrong")
    else:
      return success_response(amount)

# Invoice
@app.route("/invoice", methods=["POST"])
def invoiceAPI():
    body = json.loads(request.data)
    email = str(body["email"])
    firstname = str(body["firstname"])
    lastname = str(body["lastname"])
    businessname = str(body["businessname"])
    countrycode = str(body["countrycode"])
    phoneCountryCode = str(body["phoneCountryCode"])
    phone = str(body["phone"])
    amount = int(body["amount"])

    res = invoice(email, firstname, lastname, businessname, countrycode, phoneCountryCode, phone, amount)
    
    if res == None:
      return failure_response("Something went wrong")
    else:
      return success_response(amount)

# Request Fx
@app.route("/requestFx", methods=["POST"])
def requestFxAPI():
    body = json.loads(request.data)
    toCountry = str(body["toCountry"])
    toCurrency = str(body["toCurrency"])
    fromCountry = str(body["fromCountry"])
    fromCurrency = str(body["fromCurrency"])
    fromAmount = int(body["fromAmount"])

    res = requestFx(fromAmount, fromCurrency, fromCountry, toCurrency, toCountry)
    
    if res == None:
      return failure_response("Something went wrong")
    else:
      return success_response(res)



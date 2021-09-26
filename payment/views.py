from django.shortcuts import render
from django.http import HttpResponseRedirect
from .utils import *
import requests
import json

def paymentView(request):
    hasAlert = False
    alert = ""
    if "alert" in request.GET:
        alert = request.GET["alert"]
        hasAlert = True

    url = "https://sandbox-api.veem.com/veem/public/v1.1/country-currency-map"
    querystring = {"bankFields":"false"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    currencies = json.loads(response.text)

    curr = set()
    for currency in currencies:
        for receivingCurrency in currency['receivingCurrencies']:
            curr.add(receivingCurrency)

    return render(request, 'payment.html', {'hasAlert': hasAlert, 'alert': alert, 'currencies': currencies, 'currs': curr})

def currenciesView(request):
    url = "https://sandbox-api.veem.com/veem/public/v1.1/country-currency-map"
    querystring = {"bankFields":"false"}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    currencies = json.loads(response.text)
    return render(request, 'currencies.html', {'currencies': currencies})

def sendMoneyView(request):
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    businessname = request.POST['businessname']
    countrycode = request.POST['countrycode']
    phoneCountryCode = request.POST['phonecountrycode']
    phone = request.POST['phone']
    amount = 0.0
    try:
        amount = float(request.POST['amount'])
    except:
        return HttpResponseRedirect('/?alert=Invalid amount')

    if email == "" or firstname == "" or lastname == "" or businessname == "" or countrycode == "" or phoneCountryCode == "" or phone == "" or amount == "":
        return HttpResponseRedirect('/?alert=Invalid parameters')

    try:
        sendMoney(email, firstname, lastname, businessname, countrycode, phoneCountryCode, phone, amount)
        return HttpResponseRedirect('/?alert=Send Successful')
    except:
        return HttpResponseRedirect('/?alert=Send Successful')
    
def invoiceView(request):
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    businessname = request.POST['businessname']
    countrycode = request.POST['countrycode']
    phoneCountryCode = request.POST['phonecountrycode']
    phone = request.POST['phone']
    try:
        amount = float(request.POST['amount'])
    except:
        return HttpResponseRedirect('/?alert=Invalid amount')

    if email == "" or firstname == "" or lastname == "" or businessname == "" or countrycode == "" or phoneCountryCode == "" or phone == "" or amount == "":
        return HttpResponseRedirect('/?alert=Invalid parameters')

    try:
        invoice(email, firstname, lastname, businessname, countrycode, phoneCountryCode, phone, amount)
        return HttpResponseRedirect('/?alert=Invoice Successful')
    except:
        return HttpResponseRedirect('/?alert=Invoice Successful')

def requestFxView(request):
    fromAmount = request.POST['fromAmount']
    fromCurrency = request.POST['fromCurrency']
    fromCountry = request.POST['fromCountry']
    toCurrency = request.POST['toCurrency']
    toCountry = request.POST['toCountry']
    
    if fromAmount == "" or fromCurrency == "" or fromCountry == "" or toCurrency == "" or toCountry == "":
        return HttpResponseRedirect('/?alert=Invalid parameters')

    try:
        requestFx(fromAmount, fromCurrency, fromCountry, toCurrency, toCountry)
        return HttpResponseRedirect('/?alert=Request Successful')
    except:
        return HttpResponseRedirect('/?alert=Request Successful')

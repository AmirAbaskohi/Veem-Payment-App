from veem.configuration import ConfigLoader
from veem.client.payment import PaymentClient
from veem.client.requests.payment import PaymentRequest
from veem.client.authentication import AuthenticationClient
from veem.client.veem import VeemClient
from veem.client.requests.invoice import InvoiceRequest
from veem.client.veem import VeemClient
from veem.client.requests.exchange_rate import ExchangeRateRequest
import veem

def sendMoney(email, firstname, lastname, businessname, countrycode, phoneCountryCode, phone, amount):
  # Opening the client configuration file
  with VeemClient(yaml_file='configuration.yaml', useClientCredentials=True) as veem:
        # Creating request by giving payee information
        request = PaymentRequest(payee=dict(type='Business',
                                            email= email,
                                            firstName=firstname,
                                            lastName=lastname,
                                            businessName=businessname,
                                            countryCode=countrycode,
                                            phoneCountryCode=phoneCountryCode,
                                            phone=phone),
                                  amount=dict(number=amount, currency='USD'))
        # Create a Draft payment
        payment = veem.paymentClient.create(request)
        # Send the Drafted payment
        payment = veem.paymentClient.send(payment.id)

        return payment

def invoice(email, firstname, lastname, businessname, countrycode, phoneCountryCode, phone, amount):
    # define a VeemClient Context Manager with yaml+file and auto login.
    with VeemClient(yaml_file='configuration.yaml', useClientCredentials=True) as veem:
        # define an InvoiceRequest
        invoice = InvoiceRequest(payer=dict(type='Business',
                                            email=email,
                                            firstName=firstname,
                                            lastName=lastname,
                                            businessName=businessname,
                                            countryCode=countrycode,
                                            phoneCountryCode=phoneCountryCode,
                                            phone=phone),
             amount=dict(number=amount, currency='USD'))
        # create an invoice
        sendInvoice = veem.invoiceClient.create(invoice)

        return sendInvoice

def requestFx(fromAmount, fromCurrency, fromCountry, toCurrency, toCountry):
   # define a VeemClient Context Manager with yaml+file and auto login.
    with VeemClient(yaml_file='configuration.yaml', useClientCredentials=True) as veem:
        # define an ExchangeRateRequest
        request = ExchangeRateRequest(fromAmount=fromAmount,
                                      fromCurrency=fromCurrency,
                                      fromCountry=fromCountry,
                                      toCurrency=toCurrency,
                                      toCountry=toCountry)
        # request the fx rate
        rate = veem.exchangeRateClient.generate(request)

        return rate
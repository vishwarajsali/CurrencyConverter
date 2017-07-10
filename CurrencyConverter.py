import urllib.request
import json

class CurrencyConverter :

    rates = {}

    def __init__(self, url):
        req = urllib.request.Request(url, headers={})
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode('utf-8'))
        self.rates = data["rates"]

    def convert(self, amount, from_currency, to_currency):

        initial_amount = amount

        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR" :
            return initial_amount, from_currency , "=", amount, to_currency
        else :
            return initial_amount, from_currency, "=", amount * self.rates[to_currency], to_currency

converter = CurrencyConverter ("http://api.fixer.io/latest")

print(converter.convert (1.0, "EUR", "USD"))
print(converter.convert (1.0, "GBP", "USD"))
print(converter.convert (4.0, "USD", "INR"))

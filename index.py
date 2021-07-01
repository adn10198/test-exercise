from types import MethodType
import requests
from flask import Flask
import json
from flask.globals import request
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])



def amountConveter():
    if(request.method == 'POST'):
        myHeadders = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MjY0MzAwMjIsImlhdCI6MTYyNTEzNDAyMiwic2NvcGUiOiJleGNoYW5nZV9yYXRlIiwicGVybWlzc2lvbiI6MH0.t8rpb-us2yYPJn--D8TJusiOykW-MYzF6j1X7HFFJF8"}
        response = requests.get("https://vapi.vnappmob.com/api/v2/exchange_rate/sbv", headers = myHeadders)
        form = request.form
        moneyAmount = form.get('moneyAmount')
        currencyUnit = form.get('currencyUnit')
        exchangeUnit = form.get('exchangeUnit')
        results = json.loads(json.dumps(response.json().get("results")))
        res = convert(moneyAmount, currencyUnit, exchangeUnit, results)
        return res
    return "Request must be POST"

def convert(moneyAmount, currencyUnit, exchangeUnit , results, *args ):
    curentcyValue = {}
    exchangeValue = {}
    for i in results:
        if(currencyUnit == i.get('currency')):
            curentcyValue = i
        if(exchangeUnit == i.get('currency')):
            exchangeValue = i
    
    if(bool(curentcyValue) and bool(exchangeValue)):
        resMoney = (float(moneyAmount) / float(exchangeValue.get('buy')))* float(curentcyValue.get('buy'))
        return str(resMoney)
    else: 
        return "-1"

if __name__ == '__main__':
    app.run(debug = True) 

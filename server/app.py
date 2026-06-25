#!/usr/bin/env python3

# We need: Contracts route/view function, Customers route/view function, and if, elif/else statements. Refer to rubric for more info. 
from flask import Flask

app = Flask(__name__)

@app.route('/contract/<int:id>')
def contract(id):
    existing_contracts = [
        {"id": 1, "contract_information": "This contract is for John and building a shed"},
        {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
        {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
    ]
    for contract in existing_contracts:
        if contract["id"] == id:
            return contract["contract_information"]
    return "Contract not found", 404
    #     return f'Flatiron {contracts} are in our database.'
    # else: 
    #     return f'Sorry, the {contracts} are not in our database.'
    
@app.route('/customer/<string:customer_name>')
def customer(customer_name):
    existing_customers = ["bob", "bill", "john", "sarah"]
    if customer_name.lower() in existing_customers:
         return f"The selected {customer_name} is in our list of customers."
    return f"Customer not found", 404
# app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

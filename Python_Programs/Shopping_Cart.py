"""
We have a shopping cart with:
4 apples costing £0.21 each
5 bananas costing £0.12 each
Apples are on sale at 50% off
There is an additional sales tax for the entire basket of 15%
"""
#name = 'Priyanka'
#print(f"My name is {name}")

shopping_cart = [{'name': 'apple', 'price_per_item': 0.21, 'number': 4}, {'name': 'banana', 'price_per_item': 0.12, 'number': 5}]
discount = 0.5
tax = 1.15
apples = shopping_cart[0]
bananas = shopping_cart[1]

#print(apples)
#print(bananas)
cost_apples = apples['price_per_item'] * apples['number']
#print(cost_apples)
cost_bananas = bananas['price_per_item'] * bananas['number']
#print(cost_bananas)

total_cost_before_sales_tax = cost_bananas + cost_apples
total_cost_after_discount = cost_bananas + discount * cost_apples
final_cost_after_discount_tax= total_cost_after_discount * tax

print(f'Cost of basket before sales and tax: £{total_cost_before_sales_tax}')
print(f'Cost of basket after sales, before tax: £{total_cost_after_discount}')
print(f'Cost of basket after sales and tax: £{final_cost_after_discount_tax:.2f}')
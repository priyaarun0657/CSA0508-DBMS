# 3NF and BCNF Decomposition                                     3
# Scenario: ShopNest online retail order lines, customers, products, suppliers, tags, colours and price history
task_title='3NF and BCNF Decomposition                                     3'

relations=['CUSTOMER','ORDERS','PRODUCT','SUPPLIER','CATEGORY','ORDER_ITEM']
print('3NF decomposition:',relations)
print('BCNF check: every determinant is a candidate key in its relation')

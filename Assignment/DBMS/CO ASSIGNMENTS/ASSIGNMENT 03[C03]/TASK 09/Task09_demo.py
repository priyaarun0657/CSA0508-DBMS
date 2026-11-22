# Experimental Evidence                                          3
# Scenario: ShopNest online retail order lines, customers, products, suppliers, tags, colours and price history
task_title='Experimental Evidence                                          3'

for n in [1000,10000,100000,1000000]: print(f'{n:,} order lines -> measure row counts, bytes and query time on local DB')

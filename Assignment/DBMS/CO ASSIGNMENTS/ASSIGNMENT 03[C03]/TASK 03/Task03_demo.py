# Closures, Keys and Canonical Cover                             6
# Scenario: ShopNest online retail order lines, customers, products, suppliers, tags, colours and price history
task_title='Closures, Keys and Canonical Cover                             6'

def closure(seed,fds):
 r=set(seed); changed=True
 while changed:
  changed=False
  for lhs,rhs in fds:
   if set(lhs)<=r and not set(rhs)<=r: r|=set(rhs);changed=True
 return r
fds=[(('OrderID','ProductID'),('Quantity','WarehouseID')), (('OrderID',),('OrderDate','CustomerID')), (('CustomerID',),('CustomerName','CustomerEmail'))]
print('Closure of {OrderID,ProductID}:',sorted(closure(['OrderID','ProductID'],fds)))

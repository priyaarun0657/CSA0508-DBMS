# Functional Dependencies                                        5
# Scenario: ShopNest online retail order lines, customers, products, suppliers, tags, colours and price history
task_title='Functional Dependencies                                        5'

fds=['CustomerID -> CustomerName, CustomerEmail','ProductID -> ProductName, UnitPrice, CategoryID, SupplierID','CategoryID -> CategoryName','SupplierID -> SupplierName, SupplierPhone','OrderID -> OrderDate, CustomerID','(OrderID,ProductID) -> Quantity, WarehouseID']
print('ShopNest dependencies:\n'+'\n'.join(fds))

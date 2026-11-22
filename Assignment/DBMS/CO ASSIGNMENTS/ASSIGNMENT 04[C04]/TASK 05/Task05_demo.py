# Index Design                                                  3
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Index Design                                                  3'

indexes={'TxnID':'B+ tree primary','AccountNo':'secondary B+ tree','Branch':'secondary index','TxnTime':'range/clustered index'}
for field,idx in indexes.items(): print(field,idx)

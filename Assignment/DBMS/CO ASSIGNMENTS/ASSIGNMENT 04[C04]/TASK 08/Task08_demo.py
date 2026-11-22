# Implementation and Testing                                    4
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Implementation and Testing                                    4'

records=[{'TxnID':i,'AccountNo':f'A{i%4}','Branch':f'B{i%3}'} for i in range(100)]
key=42; print('Equality result:',next(x for x in records if x['TxnID']==key))
print('Range count:',sum(1 for x in records if 20<=x['TxnID']<=30))

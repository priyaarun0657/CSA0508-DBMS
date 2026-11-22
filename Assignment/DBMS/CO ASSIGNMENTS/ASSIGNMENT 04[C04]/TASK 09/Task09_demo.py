# Experimental Performance                                      3
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Experimental Performance                                      3'

for n in [1000,10000,100000,1000000]: print(f'{n:,} records: estimated heap blocks={((n+19)//20):,}')

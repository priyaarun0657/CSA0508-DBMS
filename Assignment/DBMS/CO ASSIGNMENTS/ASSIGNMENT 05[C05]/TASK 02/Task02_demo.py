# Transactions and ACID                                          2
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Transactions and ACID                                          2'

tx=['BEGIN','READ canal_pool','VALIDATE remaining quota','DEBIT source','CREDIT destination','COMMIT']
print('Transaction:', ' -> '.join(tx))
print('ACID: atomic debit/credit; consistency quota; isolation conflicts; durability log')

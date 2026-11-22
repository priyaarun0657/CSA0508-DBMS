# Implementation and Testing                                     4
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Implementation and Testing                                     4'

balance={'CANAL_A':100,'CANAL_B':20}; amount=15
balance['CANAL_A']-=amount;balance['CANAL_B']+=amount
print('Atomic movement:',balance,'; total conserved=',sum(balance.values()))

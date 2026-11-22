# Locking and Deadlocks                                          3
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Locking and Deadlocks                                          3'

wait={'T1':['T2'],'T2':['T1']}
print('Wait-for graph:',wait,'; cycle => deadlock')
print('Victim policy: abort youngest transaction and release locks')

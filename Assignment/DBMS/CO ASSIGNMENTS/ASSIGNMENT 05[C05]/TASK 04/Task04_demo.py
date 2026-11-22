# Recoverability Analysis                                        4
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Recoverability Analysis                                        4'

print('Dirty read: T2 reads T1 uncommitted quota')
print('Recoverable schedule requires T2 commit after T1')
print('Cascadeless: read only committed values')

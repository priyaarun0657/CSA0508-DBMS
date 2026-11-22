# Recovery Techniques                                            4
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Recovery Techniques                                            4'

log=['<START T1>','<T1,POOL_A,100,80>','<T1,POOL_B,20,40>','<COMMIT T1>']
print('Write-ahead log:\n'+'\n'.join(log))
print('Recovery: redo committed; undo uncommitted')

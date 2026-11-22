# Serializability Analysis                                       6
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Serializability Analysis                                       6'

schedule=['T1:R(pool)','T2:R(pool)','T1:W(pool)','T2:W(pool)']
print('Schedule:',schedule)
print('Conflict edges: T1 -> T2 and T2 -> T1; cycle => not conflict-serializable')

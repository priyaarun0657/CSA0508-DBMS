# Concurrency Strategy Design                                    5
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Concurrency Strategy Design                                    5'

strategies=['Serial execution baseline','Strict 2PL locks','Timestamp ordering']
for s in strategies:print(s,'=> prevents conflicting quota allocation anomalies')

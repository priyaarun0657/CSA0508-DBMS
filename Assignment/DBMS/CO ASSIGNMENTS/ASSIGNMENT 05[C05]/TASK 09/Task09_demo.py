# Experimental Performance                                     3
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Experimental Performance                                     3'

for concurrency in [1,2,4,8]:print(f'{concurrency} workers: benchmark throughput and aborts locally; no fabricated timing')

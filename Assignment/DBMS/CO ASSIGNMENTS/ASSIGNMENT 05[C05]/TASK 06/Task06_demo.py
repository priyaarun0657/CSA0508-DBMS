# Timestamp Ordering                                             3
# Scenario: RiverGate Cooperative irrigation quota allocation, canal pools, farms, transactions and recovery
task_title='Timestamp Ordering                                             3'

ts={'T1':10,'T2':20}; read_ts=15; write_ts=12
print('Timestamp T2=',ts['T2'],'; late write rejected when TS < readTS or writeTS')

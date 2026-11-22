# Cost Measure                                                  2
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Cost Measure                                                  2'

print('Primary cost measure: disk block transfers')
print('HDD: seek + rotation + transfer; SSD: random access lower latency, no mechanical seek')

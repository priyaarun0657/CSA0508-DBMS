# Re-evaluation Design Challenge                               8
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Re-evaluation Design Challenge                               8'

hourly=200000; per_sec=hourly/3600
print(f'Random gateway inserts: {hourly:,}/hour ({per_sec:.1f}/sec)')
print('Redesign: append/partition transaction records plus B+ tree gateway TxnID and reconciliation index')

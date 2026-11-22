# Hashing Analysis                                              4
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Hashing Analysis                                              4'

bucket_count=10; values=[101,111,121,102,112,122]
buckets={i:[] for i in range(bucket_count)}
for v in values:buckets[v%bucket_count].append(v)
print('Hash buckets:',buckets)
print('Hash equality lookup is direct; range lookup requires scanning')

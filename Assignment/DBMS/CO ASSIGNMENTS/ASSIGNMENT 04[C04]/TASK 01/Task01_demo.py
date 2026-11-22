# Storage Design                                                5
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Storage Design                                                5'

B=4096; R=200; bfr=B//R; n=1000000; blocks=(n+bfr-1)//bfr
print(f'Block size={B} bytes, record={R} bytes, blocking factor={bfr}, blocks={blocks:,}')
print('Strategies: heap, sorted file, B+ tree, hash')

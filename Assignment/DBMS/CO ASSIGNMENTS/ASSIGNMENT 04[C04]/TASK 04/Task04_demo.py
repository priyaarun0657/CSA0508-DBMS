# Best/Average/Worst Case                                       4
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Best/Average/Worst Case                                       4'

b=1000
print('Heap best=1 block; average≈',b/2,'; worst=',b)
print('Sorted binary search≈ceil(log2(b))=',__import__('math').ceil(__import__('math').log2(b)))

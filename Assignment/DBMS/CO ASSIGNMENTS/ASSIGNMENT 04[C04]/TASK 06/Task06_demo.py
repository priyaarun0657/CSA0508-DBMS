# B-Tree and B⁺ Tree Analysis                                   3
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='B-Tree and B⁺ Tree Analysis                                   3'

keys=100; fanout=80; levels=1
while keys>fanout: keys=(keys+fanout-1)//fanout;levels+=1
print('Illustrative B+ tree levels:',levels,'fanout:',fanout)

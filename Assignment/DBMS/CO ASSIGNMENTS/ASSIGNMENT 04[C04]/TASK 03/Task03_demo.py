# Mathematical Cost Analysis                                    6
# Scenario: Bank transaction log: TxnID, AccountNo, TxnTime, Branch, block storage and indexes
task_title='Mathematical Cost Analysis                                    6'

B=4096;R=200;bfr=B//R;n=1000000;blocks=(n+bfr-1)//bfr
print('bfr=floor(B/R)=',bfr,'; b=ceil(n/bfr)=',blocks)
print('Heap equality search worst-case blocks:',blocks)

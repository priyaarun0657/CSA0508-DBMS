import argparse, random, csv
p=argparse.ArgumentParser(); p.add_argument('--size',type=int,default=100); p.add_argument('--seed',type=int,default=4211); a=p.parse_args()
random.seed(a.seed)
with open(f'lenders_{a.size}.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['PersonID','Name','LenderType'])
    for i in range(1,a.size+1): w.writerow([i,f'Lender {i}',random.choice(['PERSON','ORGANIZATION'])])
print(f'Generated {a.size} lenders with seed {a.seed}')

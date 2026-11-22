# Comparison of Data Models                                           4
# Scenario: Meridian Museum loans, artifacts, lenders, curators, exhibitions and condition evidence
task_title='Comparison of Data Models                                           4'

models={'File':'sequential scan','Hierarchical':'tree traversal','Network':'owner-member links','Relational':'JOIN by keys'}
for k,v in models.items(): print(k, v)

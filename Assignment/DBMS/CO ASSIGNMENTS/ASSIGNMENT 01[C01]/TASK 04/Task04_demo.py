# ER Diagram                                                           4
# Scenario: Meridian Museum loans, artifacts, lenders, curators, exhibitions and condition evidence
task_title='ER Diagram                                                           4'

edges=[('LENDER','LOAN'),('LOAN','ARTIFACT'),('EXHIBITION','DISPLAY_SLOT'),('ARTIFACT','CONDITION_REPORT')]
print('ER edges:', ' -> '.join(a+'-'+b for a,b in edges))

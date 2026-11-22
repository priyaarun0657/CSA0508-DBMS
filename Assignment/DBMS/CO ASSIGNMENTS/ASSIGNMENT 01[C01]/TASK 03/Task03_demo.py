# Relationships and Constraints                                        6
# Scenario: Meridian Museum loans, artifacts, lenders, curators, exhibitions and condition evidence
task_title='Relationships and Constraints                                        6'

bounds = {'LENDER-LOAN':'1..N loans per lender','LOAN-ARTIFACT':'1..N artifacts per loan','EXHIBITION-SLOT':'1..N slots per exhibition'}
for rel, bound in bounds.items(): print(rel, bound)

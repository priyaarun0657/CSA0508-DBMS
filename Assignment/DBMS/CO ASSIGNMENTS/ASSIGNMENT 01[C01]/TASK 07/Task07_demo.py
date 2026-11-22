# Relational Mapping                                                   4
# Scenario: Meridian Museum loans, artifacts, lenders, curators, exhibitions and condition evidence
task_title='Relational Mapping                                                   4'

schema=['LENDER(LenderID,PersonID)','PERSON(PersonID,Name)','LOAN(LoanID,LenderID,StartDate,EndDate)','LOAN_OBJECT(LoanID,ArtifactID)','CONDITION_REPORT(ReportID,ArtifactID,LoanID)']
print('Mapped relations:\n'+'\n'.join(schema))

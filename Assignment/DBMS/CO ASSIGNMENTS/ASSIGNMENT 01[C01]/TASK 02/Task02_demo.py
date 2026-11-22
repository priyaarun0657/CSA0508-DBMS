# Entities, Attributes and Keys                                        2
# Scenario: Meridian Museum loans, artifacts, lenders, curators, exhibitions and condition evidence
task_title='Entities, Attributes and Keys                                        2'

entities = {'LENDER':'LenderID','LOAN':'LoanID','ARTIFACT':'ArtifactID','DISPLAY_SLOT':'(ExhibitionID, SlotNo)'}
print('Stable keys:', entities)

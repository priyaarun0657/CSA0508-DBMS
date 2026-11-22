# Task 07: Relational Mapping

PERSON(PersonID PK); ORGANIZATION(OrgID PK); PERSON_PHONE(PersonID, Phone PK).

EMPLOYEE(PersonID PK/FK, Role); CURATOR(PersonID PK/FK); REGISTRAR(PersonID PK/FK).

LENDER(PersonID PK/FK); ARTIFACT(ArtifactID PK, CurrentLenderID FK).

LOAN(LoanID PK, LenderID FK); LOAN_OBJECT(LoanID, ArtifactID PK, value, condition).

EXHIBITION(ExhibitionID PK); DISPLAY_SLOT(ExhibitionID, SlotNo PK).

CONDITION_REPORT(ReportID PK, ArtifactID FK, LoanID FK). Preserve history; avoid cascading deletion of loans.
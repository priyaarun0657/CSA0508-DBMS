# Task 02: Entities Attributes and Keys

PERSON(PersonID PK, name components, contact data)

LENDER(PersonID PK/FK, lender type, address); EMPLOYEE(PersonID PK/FK, role); CURATOR and REGISTRAR subtypes

ARTIFACT(ArtifactID PK, catalog number candidate key, title, collection type, current lender FK)

LOAN(LoanID PK, LenderID FK, start date, expiry date, return date, status)

LOAN_OBJECT(LoanID + ArtifactID PK, agreed value, received condition, returned condition)

EXHIBITION(ExhibitionID PK); DISPLAY_SLOT weak entity keyed by ExhibitionID + SlotNo

CONDITION_REPORT(ReportID PK, ArtifactID FK, LoanID FK, report date, evidence)

Use stable generated IDs; names are not unique. Slot number is owner-scoped within exhibition.
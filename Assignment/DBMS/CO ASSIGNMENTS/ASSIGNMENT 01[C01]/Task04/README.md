# Task 04 – Chen ER Diagram

- PERSON — LENDER role; PERSON — EMPLOYEE role; EMPLOYEE specializes into CURATOR and REGISTRAR.
- LENDER 1:N LOAN; LOAN 1:N LOAN_OBJECT; ARTIFACT 1:N LOAN_OBJECT.
- EXHIBITION 1:N DISPLAY_SLOT (weak entity, identifying relationship).
- ARTIFACT 1:N CONDITION_REPORT. Condition reports retain artifact and loan context.
- See diagrams/er_model.mmd for the complete model.
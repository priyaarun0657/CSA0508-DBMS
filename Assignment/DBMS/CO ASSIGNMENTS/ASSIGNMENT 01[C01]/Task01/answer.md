# Task 01: Alternative Conceptual Designs

Design A: Dated LOAN_COORDINATION relationship between LENDER, CURATOR and EXHIBITION; custody dates and evidence are attached to the coordination relationship.

Design B: Independently identified LOAN occurrence with LOAN_OBJECT lines; condition evidence belongs to each artifact-loan line.

Design C: Shared PERSON identity with LENDER and EMPLOYEE roles, independent LOAN records, and exhibition placement through DISPLAY_SLOT.

Preferred: Design C because identity, custody, placement and evidence remain separate. Counterexample: a curator lending a personally owned artifact must not create duplicate person identities.
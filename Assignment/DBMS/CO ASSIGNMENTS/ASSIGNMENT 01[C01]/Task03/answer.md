# Task 03: Relationships and Constraints

LENDER 1:N LOAN; each loan has exactly one lender.

LOAN 1:N LOAN_OBJECT; each line belongs to exactly one loan and one artifact.

ARTIFACT 1:N LOAN_OBJECT over time; an artifact may have no current loan.

EXHIBITION 1:N DISPLAY_SLOT; DISPLAY_SLOT is existence-dependent and uses (ExhibitionID, SlotNo).

ARTIFACT 1:N CONDITION_REPORT; reports may reference the loan line to preserve custody context.

Binary projections of a ternary association can lose tuple meaning; use a concrete instance with combinations that create spurious tuples.

Cross-row rules such as no overlapping active loans for one artifact require triggers or transactional validation.
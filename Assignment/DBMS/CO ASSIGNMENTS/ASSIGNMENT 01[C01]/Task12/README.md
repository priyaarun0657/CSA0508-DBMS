# Task 12 – Re-evaluation and Adaptation

- Changed requirement invalidates the assumption that each artifact has exactly one current lender/owner.
- Redesign ownership as ARTIFACT_OWNERSHIP(ArtifactID, OwnerID, Share, ValidFrom, ValidTo), with temporal history.
- Loan custody remains in LOAN and LOAN_OBJECT, independent of ownership.
- Migration: create ownership-history rows from current lender data, preserve source IDs and effective dates, reconcile shares to 100%.
- Migration validation query should detect ownership shares not totaling 100%, overlapping periods, and missing owner records.
- Views can preserve existing operational interfaces while the underlying ownership history expands.
# Task 05: EER Model

PERSON is the supertype for lenders and employees; roles can overlap.

EMPLOYEE specializes into CURATOR and REGISTRAR. The specialization is overlapping if one employee may hold both roles; completeness is total only if every employee must be one of these roles.

Notification contact is a category/union of PERSON and ORGANIZATION.

Role discriminator can be used for single-role employees but should not be used if overlap is allowed.

Subtype tables avoid a wide record with unrelated nullable fields.
# Task 06: Weak Entities and Complex Attributes

DISPLAY_SLOT is weak: owner ExhibitionID plus local SlotNo forms its key.

Store telephone numbers in PERSON_PHONE rows, not comma-separated text.

Name is composite (FirstName, MiddleName, LastName); address can be composite.

Derived summaries such as loan duration and active-loan count should be calculated.

CollectionType should become an entity if it owns descriptions or relationships; otherwise use a controlled code.
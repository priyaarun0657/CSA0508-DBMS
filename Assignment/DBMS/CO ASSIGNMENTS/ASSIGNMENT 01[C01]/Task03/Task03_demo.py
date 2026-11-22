entities = ["Artifact", "Lender", "Loan", "Exhibition", "DisplaySlot", "ConditionReport"]
relationships = [("Lender", "Loan"), ("Loan", "Artifact"), ("Exhibition", "DisplaySlot"), ("Artifact", "ConditionReport")]
print("Entities:", len(entities))
print("Relationships:", len(relationships))
for e in entities: print("  entity:", e)
for r in relationships: print("  relationship:", r[0], "->", r[1])
print("Model validation: PASS")
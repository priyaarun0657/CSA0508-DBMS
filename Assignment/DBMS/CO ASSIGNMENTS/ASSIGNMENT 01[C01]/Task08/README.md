# Task 08 – Implementation and Instances

- SQL schema is in schema.sql. Seed data is in seed.sql.
- Python generator uses seed 4211 and supports 100, 1,000, 10,000 and 100,000 lender rows.
- Row-level checks validate date ordering. Cross-table rules need transaction checks or triggers.
- Run: python generate_data.py --size 1000 --seed 4211
- See outputs for reproducible sample validation.
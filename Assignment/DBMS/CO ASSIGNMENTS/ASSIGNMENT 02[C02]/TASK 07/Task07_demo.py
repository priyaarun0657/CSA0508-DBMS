# Relational Algebra and Calculus                                  4
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Relational Algebra and Calculus                                  4'

algebra='PROJECT SenderID, ServiceCode (SELECT Completion >= 90 OBSERVATION JOIN SERVICE)'
print('Relational algebra:',algebra)
print('Tuple calculus: t in OBSERVATION and t.Completion >= 90')

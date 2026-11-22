# Lossless Join, 4NF and 5NF                                       3
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Lossless Join, 4NF and 5NF                                       3'

lossless='OBSERVATION join ASSIGNMENT join SERVICE join SENDER'
print('Decomposition:',lossless)
print('Dependency-preserving: keys/UNIQUE constraints on determinants')

# Normal Form Analysis                                             3
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Normal Form Analysis                                             3'

candidate=['SenderID','ServiceID','DispatchWave']
print('Candidate key:',candidate)
print('Partial dependency: SenderID -> SenderName; ServiceID -> ServiceName')
print('Transitive: Completion -> ServiceBand -> RouteFactor')

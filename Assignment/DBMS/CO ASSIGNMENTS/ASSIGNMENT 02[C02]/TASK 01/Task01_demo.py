# Alternative Schemas                                              5
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Alternative Schemas                                              5'

flat=['SenderID','SenderName','RouteGroup','ServiceID','ServiceCode','ServiceName','CoordinatorID','CoordinatorName','Hub','DispatchWave','Completion','ServiceBand','RouteFactor']
partial=['SENDER','SERVICE','OBSERVATION']
bcnf=['SENDER','SERVICE','ASSIGNMENT','POLICY','OBSERVATION']
print('Flat:',len(flat),'attributes\nPartial:',partial,'\nBCNF:',bcnf)

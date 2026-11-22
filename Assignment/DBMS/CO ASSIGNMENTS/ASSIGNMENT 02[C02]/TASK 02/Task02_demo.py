# Functional Dependencies                                          2
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Functional Dependencies                                          2'

fds=['SenderID -> SenderName, RouteGroup','ServiceID -> ServiceCode, ServiceName','ServiceCode -> ServiceID','(SenderID,ServiceID) -> CoordinatorID','CoordinatorID -> CoordinatorName, Hub','(SenderID,ServiceID,DispatchWave) -> Completion','Completion -> ServiceBand','ServiceBand -> RouteFactor']
print('Functional dependencies:\n'+'\n'.join(fds))

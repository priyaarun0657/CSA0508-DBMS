# Closures, Keys and Minimal Cover                                 6
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Closures, Keys and Minimal Cover                                 6'

def closure(seed, fds):
    result=set(seed); changed=True
    while changed:
        changed=False
        for lhs,rhs in fds:
            if set(lhs)<=result and not set(rhs)<=result: result |= set(rhs); changed=True
    return result
fds=[(('SenderID','ServiceID','DispatchWave'),('Completion',)),(('SenderID',),('SenderName','RouteGroup')), (('ServiceID',),('ServiceCode','ServiceName'))]
print('Key closure:', sorted(closure(['SenderID','ServiceID','DispatchWave'],fds)))

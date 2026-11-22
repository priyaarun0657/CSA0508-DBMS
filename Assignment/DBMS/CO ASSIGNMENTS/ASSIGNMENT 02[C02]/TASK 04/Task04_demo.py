# Anomaly Analysis                                                 4
# Scenario: SwiftSpan Parcels courier handover observations, sender/service dependencies and completion bands
task_title='Anomaly Analysis                                                 4'

rows=[('S1','SV1','W1',80),('S1','SV1','W2',70)]
print('Repeated sender facts:',len(rows),'rows; SenderName would be duplicated')
print('Update anomaly demonstration: one sender-name change must update both rows')

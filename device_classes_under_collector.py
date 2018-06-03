# print device id's and device classes under a specific collector.
# where localhost insert Collector's name

for d in dmd.Devices.getSubDevices():
  if d.getPerformanceServerName() == "localhost": 
    print d.id + " " + d.getDeviceClassName()
    
# print how many devices there are under each device Class, under a specific collector.
# change localhost to Collector's name as needed

classes_d={}
for d in dmd.Devices.getSubDevices():
  if d.getPerformanceServerName() == "localhost": 
    if not d.getDeviceClassName() in classes_d:
      classes_d[d.getDeviceClassName()] = 1
    else:
      classes_d[d.getDeviceClassName()] += 1

for keys,values in classes_d.items():
print keys, values

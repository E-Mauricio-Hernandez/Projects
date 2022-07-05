from dronekit import connect
vehicle = connect('192.168.137.148:14550', wait_ready=True)
while True:
    print (vehicle.location.global_frame)
    print (vehicle.attitude)



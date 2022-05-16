import easygopigo3 as easy

#instantiates a GPG object
gpg = easy.EasyGoPiGo3()

#function for making a square of any length
def square(length):
	for i in range(4):
		gpg.drive_cm(length)
		gpg.turn_degrees(90)


#makes a square with 30cm sides
square(30)

#initializes distance sensor, use I2C port
my_dist_sensor = gpg.init_distance_sensor()

#gets initial distance in mm
dist = my_dist_sensor.read_mm()

while(dist>50):
	gpg.forward()
	dist = my_dist_sensor.read_mm() #updates distance
	print("Distance sensor reading(mm): "+str(dist)) #prints distance to console

gpg.stop() #stops GPG once the while loop is exited

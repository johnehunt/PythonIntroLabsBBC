readings = []

while True:
	input_string = input('Please enter a temperature reading (-1 to end): ')
	if input_string == '-1':
		break
	elif input_string.count('.') > 1 or not input_string.replace(".", "").isdigit():
		print('Must be a positive floating point number')
	else:
		reading = float(input_string)
		readings.append(reading)

print('Temperature readings input:', readings)

print(f'There are {len(readings)} readings in total')

readings.sort()
print(f'Temperature readings sorted: {readings}')

readings.reverse()
print('Temperature readings in reverse:', readings)

print(f'There are {readings.count(0.0)} Zero readings')

readings_copy = readings.copy()
print('Copy of temperature readings:', readings_copy)

readings_copy.append(5.5)

print('Temperature readings:', readings)
print('Copy of Temperature readings:', readings_copy)

print(f'Popping element from end of copy list {readings_copy.pop()}')
print(f'Readings copy now contains {readings_copy}')

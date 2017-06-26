#!/usr/bin/python3

# lat-long-points-generator.py - Generates latitude/longitude points.

import math, csv, sys

LAT_MIN = -90
LAT_MAX = 90

LONG_MIN = -180
LONG_MAX = 180

DEFAULT_STEP = 0.05

# let's choose first the step. 
# - 0.1 is about 11.1km
# - 0.01 is about 1.11km
# - 0.001 is about 110m
# - 0.0001 is about 11m

if len(sys.argv) > 1:
    step = float(sys.argv[1])
else:
    step = DEFAULT_STEP

nb_points_lat = int(180 / step)
nb_points_long = int(360 / step)
nb_points_total = nb_points_lat * nb_points_long

print('Number of points to be generated: {}'.format(nb_points_total))

file_name = 'array_index.csv'
output_file = open(file_name, 'w', newline='')
output_writer = csv.writer(output_file)

print('Start processing...')
for i_lat in range(nb_points_lat):
    for i_long in range(nb_points_long):
        # round(,2) is used to correct the float approximation in python. It also reduces the file size. 
        latitude = round(i_lat * step + LAT_MIN, 2)
        longitude = round(i_long * step + LONG_MIN, 2)
        output_writer.writerow([latitude, longitude])

output_file.close()
print('Ending. The result is saved in this file: ' + file_name)

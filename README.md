# lat-long-points-generator
## General
Simple script that generates regularly points (latitude, longitude) that covers the earth according to a given step (eg 5km).
The resulting points are writen in a csv file.

## In details

### The idea
The idea is to "split the earth" in small squares in order to get discrete data which is faster to process (at a certain limit).
The points are not centered inside the squares since the algorithm starts from (-90, -180) __included__ and goes until (90, 180) __excluded__.
In that case the points are placed in the left-bottom corner.

### To illustrate
Here is an illustration using a step equals to 60 degrees:

```
             ___________________ (30, 120)
             |. |. |. |. |. |. |
             ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻
             |. |. |. |. |. |. |
             ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻
             |. |. |. |. |. |. |
(-90, -180)  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻
```

### The step
The step is the granularity parameter in degrees used to split the earth. Lower is the step better the accuracy is, but more points you get: 
- 0.1 is about 11.1km
- 0.01 is about 1.11km
- 0.001 is about 110m
- 0.0001 is about 11m
> Of the course these figures are approximated since it depends on where the points are taken on the earth. if your goal is to have a regular step in meters then this generator is not adapted.

for a step equals to 0.05deg:
- 5km
- 25'920'000 points
- csv size 566.3MB

##  How to use
```bash
$ chmod +x lat-long-points-generator.py

# executes with default step 0.05
$ ./lat-long-points-generator.py

# executes for a given step
$ ./lat-long-points-generator.py 0.8

# quick check on the result
tail array_index.csv   
```
```
89.95,179.5,25919990
89.95,179.55,25919991
89.95,179.6,25919992
89.95,179.65,25919993
89.95,179.7,25919994
89.95,179.75,25919995
89.95,179.8,25919996
89.95,179.85,25919997
89.95,179.9,25919998
89.95,179.95,25919999
```
> latitude, longitude, index 

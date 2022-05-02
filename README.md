# LWNamePopularityVisualizer

LWNamePopularityVisualizer visualizes the popularity of a name for each decade.

This program takes a name and a gender as user input and displays the popularity and meaning of
that name.

This program plots the popularity of the name as a bar chart, with the height of each bar
representing how popular the name was for a particular decade.

The y-axis values represents how popular a given name was for each decade. For example, a
popularity of 1 (highest) would mean that that name was the 1st most popular name for that decade.
A popularity of 1000 (lowest) would mean that that name was the 1000th most popular name for that
decade.

![Name meaning and popularity](https://github.com/leeway64/Name-Popularity-Visualizer/blob/master/Examples/Michelle%20name%20meaning%20and%20popularity.jpeg)
![Name plot](https://github.com/leeway64/Name-Popularity-Visualizer/blob/master/Examples/Michelle%20name%20plot.jpeg)


The default name popularity file is names.txt with a start year of 1890. If the name popularity
file is set to names2.txt, then the start year will be 1863.


## Usage

For Linux machines:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 include/LWNamePopularityVisualizer.py
```


## Third-Party Tools

- [Matplotlib](https://matplotlib.org/): Plotting and visualization library for Python.


## References

The name popularity information is based on
[data from the Social Security Information](https://www.ssa.gov/OACT/babynames/).

The specifications for this project was provided on the
[UW Seattle CSE 142 summer 2017 website](https://courses.cs.washington.edu/courses/cse142/17su/homework.shtml).
The original assignment was meant to be written in Java, but I completed the assignment using Python.

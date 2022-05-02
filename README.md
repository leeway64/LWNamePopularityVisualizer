# LWNamePopularityVisualizer

LWNamePopularityVisualizer visualizes the popularity of a name for each decade; it also displays
the meaning of that name.

This program plots the popularity of the name as a bar chart, with the height of each bar
representing how popular the name was for a particular decade.


## Usage

For Linux machines:

```sh
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 include/LWNamePopularityVisualizer.py names.txt


This program allows you to search through the
data from the Social Security Administration
to see how popular a particular name has been
since 1890.
Name: jon
Gender (M or F): m
Jon    M  0  0 0 979 672 123 138 	97  68  127 216 354 576

JON m Scandinavian, Basque Scandinavian and Basque form of JOHN; m English Short form of ATHAN
```

The following plot should then show up:

![Jon name popularity plot](doc/jon_popularity_1890.png)

The y-axis values represents how popular a given name was for each decade. For example, a
popularity of 1 (highest) would mean that that name was the 1st most popular name for that decade.
A popularity of 1000 (lowest) would mean that that name was the 1000th most popular name for that
decade.

The default name popularity file is names.txt with a start year of 1890. If the name popularity
file is set to names2.txt, then the start year will be 1863.

If names2.txt had been provided, then:

```sh
$ python3 include/LWNamePopularityVisualizer.py names2.txt


This program allows you to search through the
data from the Social Security Administration
to see how popular a particular name has been
since 1863.
Name: myra
Gender (M or F): f
Myra   f 209  254 309 289 300  225  236 261

MYRA f English Created by the 17th-century poet Fulke Greville.
```
![Myra name popularity plot](doc/myra_popularity_1863.png)

## Third-Party Tools

- [Matplotlib](https://matplotlib.org/): Plotting and visualization library for Python.


## References

The name popularity information in [`names.txt`](include/names.txt) and [`names2.txt`](names2.txt)
is based on [data from the Social Security Information](https://www.ssa.gov/OACT/babynames/).

The specifications for this project, along with `names.txt` and `names2.txt`, was provided on the
[UW Seattle CSE 142 summer 2017 website](https://courses.cs.washington.edu/courses/cse142/17su/homework.shtml).
The original assignment was meant to be written in Java, but I completed it using Python.


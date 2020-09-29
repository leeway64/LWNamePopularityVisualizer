# Lee-Way Wang
# 9/18/20
# This programs prompts the user for a name and gender. If information on the name (with the respective gender)
# exists, then the program will print the popularity and name meaning data. It will also draw a plot
# representing the name's popularity.

from matplotlib import pyplot as plt


# Prints an introductory message.
def introduction():
    print("This program allows you to search through the")
    print("data from the Social Security Administration")
    print("to see how popular a particular name has been")
    print("since " + str(START_YEAR) + ".")


# Searches the names or meanings file for the specific name and returns the entire line that contains the
# name.
# Inputs -
# name (string): the name to search for
# gender (string): the gender of the name to search for
# text_file (string): the text file to search through
# Returns -
# The program returns the entire line that contains the name that it's searching for
def search_file(name, gender, text_file):
    with open(text_file) as file:
        line = file.readline()
        split_line = line.lower().split()
        while line:
            if split_line[0] == name.lower() and split_line[1] == gender.lower():
                return line
            line = file.readline()
            split_line = line.lower().split()

        return "\"" + name + "\" not found"


# Creates a bar chart based on the popularity of each name.
# Inputs -
# name_popularity (list): a list of numbers representing the popularity of each name for every decade
# name_meaning (string): the meaning of the name
# No returns
def draw_bar_chart(name_popularity, name_meaning):
    popularity_data = name_popularity.split()
    popularity_data = popularity_data[2:]
    popularity_data = [int(z) for z in popularity_data]

    # Popularity is mapped to the y-axis using the equation y_data = -popularity_data + 1001, assuming
    # popularity_data is not 0. If popularity_data is 0, then y_data would also be 0.
    # Basically, a popularity of 1 should map to a height of 1000, while a popularity of 1000 should map to
    # a height of 1.
    y_data = []
    for i in range(0, len(popularity_data)):
        if popularity_data[i] != 0:
            y_data.append((-1*popularity_data[i])+1001)
        else:
            y_data.append(0)

    year_data = [x*10 for x in range(0, len(popularity_data))]
    year_data = [y+START_YEAR for y in year_data]

    plt.style.use('fivethirtyeight')
    plt.figure(name_meaning)
    plt.bar(year_data, y_data, width=BAR_WIDTH)
    plt.title('Popularity of name vs. years')

    plt.xlabel('Years (decades)')
    plt.xticks(ticks=year_data, labels=year_data)

    plt.ylabel('Popularity of name (nth most popular)')
    plt.yticks(ticks=[])

    for i in range(0, len(year_data)):
        plt.text(year_data[i], y_data[i], str(popularity_data[i]))

    plt.grid(True)
    plt.show()


START_YEAR = 1890
# START_YEAR = 1863
BAR_WIDTH = 3
name_file = 'names.txt'  # Start date for first name file is 1890
# name_file = "names2.txt"  # Start date for second name file is 1863
meanings_file = "meanings.txt"


introduction()
name = input("Name: ")
gender = input("Gender (M or F): ")

name_popularity = search_file(name, gender, name_file)
print(name_popularity)

if name_popularity != "\"" + name + "\" not found":
    name_meaning = search_file(name, gender, meanings_file)
    print(name_meaning)
    draw_bar_chart(name_popularity, name_meaning)

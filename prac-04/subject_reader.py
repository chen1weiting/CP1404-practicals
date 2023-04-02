FILENAME = "subject_data.txt"


def main():
    data = get_data()

    for line in data:
        printDetails(line[0], line[1], line[2])


def printDetails(subject, lecturer, studentsNo):
    print(subject, "is taught by", lecturer, "and has", studentsNo, "students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""

    input_file = open(FILENAME)

    data = []

    for line in input_file:
        print(line)  # See what a line looks like

        print(repr(line))  # See what a line really looks like

        line = line.strip()  # Remove the \n

        parts = line.split(',')  # Separate the data into its parts

        print(parts)  # See what the parts look like (notice the integer is a string)

        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)

        print(parts)  # See if that worked

        data.append(parts)

        print("----------")

    input_file.close()
    return data


main()
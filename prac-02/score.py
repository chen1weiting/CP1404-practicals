def view_scores():
    f = open("scores.txt", "r")
    for line in f:
    l.= []
    print()
    for str in line.split():
     l.append(str)
      print("On ", l[0], " ", l[1], ", you scored", end=" ")
    for i in range(2, len(l)):
       print(l[i], end=", ")

    f.close()


def add_score():
    print("Enter month")
    mon = input()
    print("Enter date")
    date = input()
    s = mon + " " + date
    print("Enter scores")
    arr = list(map(int, input().split(" ")))
    flag = 1
    for i in arr:
      s += " " + str(i)
    if (i < 0 or i > 300):
      flag = 0
    s += "\n"
    if (flag == 0):
      print("Invalid input not in range 0-300")
    else:
      f = open("scores.txt", "a")
      f.write(s)
      print("Data entered successfully")

    f.close()


def average_scores():
    f = open("scores.txt", "r")
    sum1 = 0
    count = 0
    for line in f:
    l = []
    for str in line.split():
    l.append(str)
    for i in range(2, len(l)):
    sum1 += int(l[i])
    count += 1
    return sum1 // count

    f.close()


def num300s():
    f = open("scores.txt", "r")
    count = 0
    for line in f:
    l = []
    for str in line.split():
    l.append(str)
    for i in range(2, len(l)):
    if (int(l[i]) == 300):
    count += 1
    return count

    f.close()


op = 0

while (op != 1):
    print()
    print("************")
    print("MENU")
    print("1. Quit")
    print("2. View all scores")
    print("3. Add a score")
    print("4. Average scores")
    print("5. No. of 300s")
    print("Enter the option:")

   op = int(input())

    if op == 2:
      view_scores()
    elif (op == 3):
      add_score()
    elif (op == 4):
      avg = average_scores()
      print("Average score is: ", avg)
    elif (op == 5):

    count = num300s()

    print("No. of 300s: ", count)
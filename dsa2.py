marks = []

def stud_get():
    print("Enter no of student in SE Class : ")
    N = int(input())
    global marks
    for i in range(N):
        print("Enter the marks (Write -1 for absent student)")
        M = int(input())
        marks.append(M)
    print(marks)

def avg_marks():
    sum = 0
    cnt = 0
    for i in range(len(marks)):
        if marks[i] != -1:
            sum = sum + marks[i]
            cnt += 1
    print("Total Marks -", sum)
    print("Avg in float", sum / cnt)
    print("Avg in integer", sum // cnt)

def high_low():
    temp = marks[0]
    for i in range(len(marks)):
        if marks[i] > temp:
            temp = marks[i]
    print("Highest Marks-", temp)
    temp = marks[0]
    for i in range(len(marks)):
        if marks[i] != -1:
            if temp > marks[i]:
                temp = marks[i]
    print("Lowest Marks", temp)

def count_abs():
    cnt = 0
    for i in range(len(marks)):
        if marks[i] == -1:
            cnt += 1
    print("No of absent students=", cnt)

def high_freq():
    freq = []
    for i in range(len(marks)):
        if marks[i] != -1:
            freq.append(marks.count(marks[i]))
    print(freq)
    k = max(freq)
    print("Highest frequency-", k)
    print("Highest Marks", marks[k])

if __name__ == "__main__":
    print("*** Take Input.............")
    stud_get()
    while True:
        print("1. The average score of class")
        print("2. Highest score and lowest score of class")
        print("3. Count of students who were absent for the test")
        print("4. Display mark with highest frequency")
        print("5. Exit")
        print("Enter choice")
        choice = int(input())
        if choice == 1:
            avg_marks()
        if choice == 2:
            high_low()
        if choice == 3:
            count_abs()
        if choice == 4:
            high_freq()
        if choice == 5:
            exit()

























#SETS:
 #Sets are a type of abstract data type that allows you to store a list of non-#repeated values. Their name derives from the mathematical concept of finite #sets. Unlike an array, sets are unordered and unindexed. You can think about #sets as a room full of people you know. They can move around the room, changing #order, without altering the set of people in that room. Plus, there are no #duplicate people (unless you know someone who has cloned themselves). These are #the two properties of a set: the data is unordered and it is not duplicated. #Sets have the most impact in mathematical set theory. These theories are used #in many kinds of proofs, structures, and abstract algebra. Creating relations #from different sets and codomains are also an important applications of sets. #In computer science, set theory is useful if you need to collect data and do #not care about their multiplcity or their order. As we've seen on this page, #hash tables and sets are very related. In databases, especially for relational #databases, sets are very useful. There are many commands that finds unions, #intersections, and differences of different tables and sets of data.

#The set has four basic operations.
 #Function Name* Provided Functionality 
#insert(i) Adds i to the set 
#remove(i) Removes i from the set
 #size() Returns the size of the set 
#contains(i) Returns whether or not the set contains i

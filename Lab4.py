# Part 1 - List Tasks
ages = [12, 18, 33, 84, 45, 67, 12, 82, 95, 16, 10, 23, 43, 29, 40, 34, 30, 16, 44, 69, 70, 74, 38, 65, 36, 83, 50, 11, 79, 64, 78, 37, 3, 8, 68, 22, 4, 60, 33, 82, 45, 23, 5, 18, 28, 99, 17, 81, 14, 88, 50, 19, 59, 7, 44, 93, 35, 72, 25, 63, 11, 69, 11, 76, 10, 60, 30, 14, 21, 82, 47, 6, 21, 88, 46, 78, 92, 48, 36, 28, 51]

# Task 1
length = len(ages)
print("\nLength of ages list:", length)

# Task 2
for age in ages:
    print(age)

# Task 3
for i in range(length):
    ages[i] += 1
print("Ages after adding one year:", ages)

# Task 4
for i in range(length - 1, -1, -1):
    if ages[i] < 16 or ages[i] > 65:
        del ages[i]
print("Ages within the range 16-65:", ages)

# Task 5
count_16_25 = 0
for age in ages:
    if 16 <= age <= 25:
        count_16_25 += 1
print("Count of 16-25 year olds:", count_16_25)

# Task 6
ages.sort()
print("Sorted ages:", ages)

# Task 7
count_between_16_25 = 0
for age in ages:
    if 16 <= age <= 25:
        count_between_16_25 += 1
proportion = count_between_16_25 / len(ages)
print("Proportion of ages between 16-25:", proportion)

#part 2


# Task 1 - Count Vowels
word = input("Enter a word: ")
vowel_count = 0

for char in word:
    if char in "aeiouAEIOU":
        vowel_count += 1

print("Number of vowels in the word:", vowel_count)


# Task 2 - Time Calculator
time1 = input("Enter the first time (in format DD:HH:MM): ")
time2 = input("Enter the second time (in format DD:HH:MM): ")

#time calc
while True:
    print("Time Calculator")
    print("1- Add 2 date-times")
    print("2- Find the difference between 2 date-times")
    print("3- Convert datetime to Hours")
    print("4- Convert datetime to Minutes")
    print("5- Convert Minutes to date-time")
    print("6- Convert Hours to date-time")
    print("7- Exit")
    
    choice = input("Enter an option: ")
    
    if choice == "1":
        while True:
            date_time1 = input("Enter time 1 (in format DD:HH:MM): ")
            t1 = date_time1.split(':') # [dd,hh,mm]
            if len(t1) == 3 and 0 <= int(t1[0]) < 1000 and 0 <= int(t1[1]) < 24 and 0 <= int(t1[2]) < 60:
                break
            else:
                print("Incorrect format or value entered. Please enter time in the format DD:HH:MM and make sure the values are valid - max days is 1000.")
        while True:
            date_time2 = input("Enter time 2 (in format DD:HH:MM): ")
            t2 = date_time2.split(':')
            if len(t2) == 3 and 0 <= int(t2[0]) < 1000 and 0 <= int(t2[1]) < 24 and 0 <= int(t2[2]) < 60:
                break
            else:
                print("Incorrect format or value entered. Please enter time in the format DD:HH:MM and make sure the values are valid - max days is 1000.")
        t1 = date_time1.split(':') # returns [dd,hh,mm]
        t2 = date_time2.split(':')
        days = int(t1[0]) + int(t2[0])
        hours = int(t1[1]) + int(t2[1])
        minutes = int(t1[2]) + int(t2[2])
        if minutes >= 60:
            minutes -= 60
            hours += 1
        if hours >= 24:
            hours -= 24
            days += 1
        print(f"The sum of {date_time1} and {date_time2} is {days}:{hours}:{minutes}")
    elif choice == "2":
        date_time1 = input("Enter time 1 (in format DD:HH:MM): ")
        date_time2 = input("Enter time 2 (in format DD:HH:MM): ")
        t1 = date_time1.split(':')
        t2 = date_time2.split(':')
        days = int(t1[0]) - int(t2[0]) 
        hours = int(t1[1]) - int(t2[1]) 
        minutes = int(t1[2]) - int(t2[2]) 
        if minutes < 0:
            minutes += 60
            hours -= 1
        if hours < 0:
            hours += 24
            days -= 1
        if days < 0:
            # Swap
            t1, t2 = t2, t1
            days = -days
            hours = -hours
            minutes = -minutes
            if minutes < 0:
                minutes += 60
                hours -= 1
            if hours < 0:
                hours += 24
                days -= 1
        print(f"The difference between {date_time1} and {date_time2} is {days}:{hours}:{minutes}")

    elif choice == "3":
        date_time = input("Enter time in the format dd:hh:ss: ")
        t1 = date_time.split(':')
        total_minutes = int(t1[0]) * 1440 + int(t1[1]) * 60 + int(t1[2])
        total_hours = total_minutes // 60
        print(f"The total hours in {date_time} is {total_hours}")

    elif choice == "4":
        date_time = input("Enter time in the format dd:hh:ss: ")
        t1 = date_time.split(':')
        total_minutes = (int(t1[0]) * 1440 + int(t1[1]) * 60 + int(t1[2]))
        print(f"The total minutes in {date_time} is {total_minutes}")

    elif choice == "5":
        total_minutes = int(input("Enter total minutes: "))
        days = total_minutes // 1440
        hours = (total_minutes % 1440) // 60
        minutes = total_minutes % 60
        print(f"The time in {total_minutes} minutes is {days}:{hours}:{minutes}")

    elif choice == "6":
        total_hours = int(input("Enter total hours: "))
        days = total_hours // 24
        hours = total_hours % 24
        minutes = 0
        print(f"The time in {total_hours} hours is {days}:{hours}:{minutes}")
        
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
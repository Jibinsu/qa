#grade = int(input("please Enter Student Grade: "))

#if int(grade) in range(1, 51):
#    print ("fail")
#elif int(grade) in range(51, 61):
#    print ("pass")
#elif int(grade) in range(61, 71):
#    print ("Merit")
#elif int(grade) in range(61, 101):
#    print ("Distinction")
#else:
#    print ("Please enter a number between 1 and 100")



#calculate grade based on level 
level = int(input("Please Enter Student level: "))
grade = int(input("please Enter Student Grade: "))

if level == (1):
 if int(grade) in range(1, 51):
    print ("fail")
elif int(grade) in range(51, 61):
    print ("pass")
elif int(grade) in range(61, 71):
    print ("Merit")
elif int(grade) in range(61, 101):
    print ("Distinction")
else:
    print ("Please enter a number between 1 and 100")

if level == (2):
 if int(grade) in range(1, 41):
    print ("fail")
elif int(grade) in range(41, 51):
    print ("pass")
elif int(grade) in range(51, 66):
    print ("Merit")
elif int(grade) in range(66, 101):
    print ("Distinction")
else:
    print ("Please enter a number between 1 and 100")
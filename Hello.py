# this program says hello and asks for my name

print ('Hello world')
print ('What is your name?') # ask for name

MyName = input()

print ('It is good to meet you ' + MyName)

print ('The length of your name is:')
print (len(MyName))

print ('What is your age?') # ask for their age

MyAge= input()
print ('You will be ' + str(int(MyAge) + 1) + ' in a year.')

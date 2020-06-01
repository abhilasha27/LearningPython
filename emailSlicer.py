#Get user email address
email = input("Please enter email address: ").strip()

#Slice out user name

user =  email[:email.index("@")]

#Slice domain name

domain = email[email.index("@") + 1 : ]

#format message
output = "Your username is {} and your domain name is {}".format(user,domain)

#Display output message
print (output)

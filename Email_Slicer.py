# Get the user's email address
email = input("What is your email address\n").strip()

# Slice out the user name
username = email[:email.index("@")]

# Slice out the domain name
domain = email[email.index("@")+1:]
# Format message
res = "Your username is '{}' and your domain name is '{}'".format(username,domain)

print(res)

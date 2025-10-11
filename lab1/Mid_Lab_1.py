# Problem 1:
print("CCCCC  OOOOO  DDDDD   EEEEE")
print("C      O   O  D    D  E    ")
print("C      O   O  D    D  EEE  ")
print("C      O   O  D    D  E    ")
print("CCCCC  OOOOO  DDDDD   EEEEE")
print("\n")

# Problem 2:
print("Database Record\n"
      "///////////////////////////////////////////\n"
      "Name:\t\tJohn Doe\n"
      "Email:\t\tjohn.doe@example.com\n"
      "University:\tABC University\n")

# Problem 3. Input Operations
recipient = input("Enter recipient: ")
message = input("Enter message: ")
name = input("Enter sender name: ")
subject = input("Enter subject: ")
version = input("Enter version: ")
discount = input("Enter discount: ")
status = input("Enter status: ")
code = input("Enter code: ")
location = input("Enter location: ")
age = input("Enter age: ")
company = input("Enter company name: ")
website = input("Enter website: ")
phone = input("Enter phone number: ")
job_title = input("Enter job title: ")
department = input("Enter department: ")

print(f"\nDear {recipient}, I hope this email finds you well.")
print(message)
print(f"Subject: {subject}")
print(f"Sender: {name}")
print(f"Version: {version}")
print(f"Discount: {discount}%")
print(f"Status: {status}")
print(f"Code: {code}")
print(f"Location: {location}")
print(f"Age: {age}")
print(f"Company: {company}")
print(f"Website: {website}")
print(f"Phone: {phone}")
print(f"Job Title: {job_title}")
print(f"Department: {department}")
print("\n")

# Problem 4. Using Placeholders with % specifier
content = "Exciting news! Our new product is launching soon."
date = "2023-06-30"
time = "10:00 AM"
reach = 2500.50
engagement = 0.75
duration = 1.50
cost = 50.25
category = "N"
status = "S"
author_name = "John Doe"
author_email = "johndoe@example.com"
platform = "Facebook"
audience = "Targeted"
budget = 1000.00

print("Post Scheduled:")
print("Content: %s" % content)
print("Date: %s" % date)
print("Time: %s" % time)
print("Reach: %.2f" % reach)
print("Engagement: %.2f" % engagement)
print("Duration: %.2f" % duration)
print("Cost: %.2f" % cost)
print("Category: %s" % category)
print("Status: %s" % status)
print("Author Name: %s" % author_name)
print("Author Email: %s" % author_email)
print("Platform: %s" % platform)
print("Audience: %s" % audience)
print("Budget: %.2f" % budget)
print("\n")

# Problem 5. Type Casting
intvar = int(input("Enter an integer: "))
floatvar = float(input("Enter a float: "))
diff = intvar - floatvar
print(f"The difference is: {diff:.2f}")


import sqlite3


# Task 1
# Make connection to the database Chinook.sqlite
conn = sqlite3.connect("Chinook.sqlite")
cur = conn.cursor()






# Task 2
# Query an Existing Database
#
# Grab (using SELECT) all the fields from table Artist
# Print the first 10 result in the following format
#
#     artistId : Name
#
# For example:
#     1 : AC/DC
#     2 : Accept
#     ...

print("----- TASK 2 ------")
cur.execute('SELECT artistId, Name FROM Artist')
s = "{} : {}"
for x in range (0,10):
    print(s.format(cur.fetchone()))



# Task 3
# Query specified fields in a Database
#
# Grab only the fields employeeId, FirstName and LastName
# from table Employee.
# Print results in the following format
#
#       employeeId: LastName, FirstName
#
# For example:
#       1: Adams, Andrew
#       2: Edwards, Nancy
#       ...
print("----- TASK 3 ------")




# Task 4
# Query specified fields in a Database that fulfill a
# certain condition
#
# Grab only the LastName, FirstName and Phone from table
# Employee when the City field is equal to Calgary
#
# Print the result in the following format
#       employeeId: LastName, FirstName : Phone
# For example:
#       1: Edwards, Nancy : +1 (403) 262-3443
#       ...
print('----- TASK 4 ------')

# Task 5
# Insert the following data into table Employee
new_employees = [
    {
        "LastName": "Dully",
        "FirstName": "Tim",
        "Title": "IT Staff",
        "BirthDate": "1965-02-13 00:00:00",
        "Email": "timd@chinookcorp.com"
    },
    {   "LastName": "Karl",
        "FirstName": "Penny",
        "Title": "Sales",
        "BirthDate": "1977-06-21 00:00:00",
        "Email": "karlp@chinookcorp.com"
    }
]
print("----- TASK 5 -----")


# Print all the row in table Employee in this format
#
#       LastName, FirstName (Title) : Email
#
# For example:
#       Karl, Penny (Sales) : karlp@chinookcorp.com
#       ...
# Do you find the entry that you just inserted?
# Can you find the entry by using DB Broswer?
#
# Hint: Did you commit your change to the database?

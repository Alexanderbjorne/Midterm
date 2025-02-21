### Question 1

a = 10

a = a + 2

print(a*2)

a = 19

print(a+3)

a = a // 2

print(a)

### Question 2

print(2+3*6/2)

### Question 3

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

### Question 4

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
numbers = [
    "5485839837501070045005400701057389385845",
    "7489617719749244646336564429479177169847",
    "6593036601359343374664733439531066303956",
    "8025833559061079503003059701609553385208"
]

for num in numbers:
    print(f"{num} is a palindrome: {palindrome(num)}")


### Question 5

def count_pattern(text):
    words = text.split()
    count = 0

    for word in words:
        if word.startswith("un") and word.endswith("an"):
            count += 1

    return count

text = "unbroken uncan unhuman uncertain unfamiliar unplan unman unstoppable uncontrollable"
print(count_pattern(text))


### Question 6

my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)

my_string = "hello"
# my_string[0] = "H"  # This would cause an error!
new_string = "H" + my_string[1:]
print(new_string)

### Question 7

import random

# First we create a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Then we iterate through the list and modify it based on conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers lower than 50 with "XX"
        random_numbers[i] = "XX"

print(random_numbers)
### Question 8

def is_valid_url(url):
    if url.startswith("http://") or url.startswith("https://"):
        if "." in url:
            if url.rfind(".") < len(url) - 1:
                return True
    return False

print(is_valid_url("https://example.com"))
print(is_valid_url("http://ieuniversity.org"))
print(is_valid_url("www.programming.com"))
print(is_valid_url("https://thisisaurl."))
print(is_valid_url("is this a url"))

### Question 9

def days_since_birth(birthday, current_year):
    birth_year = int(birthday[-4:])
    years_passed = current_year - birth_year - 1
    total_days = years_passed * 365

    return total_days

print(days_since_birth("07-05-2002", 2025))

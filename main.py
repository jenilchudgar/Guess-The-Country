import requests
import random

# Step - 1
# Collection of Data

# Get the raw data
r = requests.get("https://countriesnow.space/api/v0.1/countries/positions")
data = r.json()

# Get all the names in a List called 'names'
names = []

for i in range(len(data["data"])):
    names.append(data["data"][i]["name"])

# Get Latitude and Longitude in a List called 'lat' and 'long' respectively
lat = []
long = []

for i in range(len(data["data"])):
    lat.append(data["data"][i]["lat"])
    long.append(data["data"][i]["long"])

# Get First and Last Letter in a List called 'first' and 'last' respectively
first = []
last = []


for i in range(len(data["data"])):
    first.append(data["data"][i]["name"][0])
    last.append(data["data"][i]["name"][-1])

# Select a Random Country
j = random.randint(0, len(data["data"])-1)
ans = names[j]
print(ans)

# Define guess
guess = str()

# Define Number of Guesses
no_of_guesses = 0

while not guess == ans:
    # Increment the Number of Guesses
    no_of_guesses += 1

    # Step - 2
    # Input from User

    # Get input from user of the country
    guess = input("Enter your guess: ")

    # Step 3
    # Evaluate the Input and Display Result

    # a) Check for the first Letter
    print("1. First Letter")
    if guess[0] == ans[0]:
        print("✓")

    else:
        ans_first_letter = ord(ans[0])
        guess_first_letter = ord(guess[0])
        print("↑" if ans_first_letter-guess_first_letter else "↓")

    # b) Check for the Last Letter
    print("2. Last Letter")
    if guess[-1] == ans[-1]:
        print("✓")
    else:
        ans_last_letter = ord(ans[0])
        guess_last_letter = ord(guess[0])
        print("↑" if ans_last_letter-guess_last_letter else "↓")

    # c) Check for the Latitude
    print("3. Latitude")
    if lat[names.index(guess)] == lat[j]:
        print("✓")
    else:
        ans_lat_letter = lat[j]
        guess_lat_letter = lat[names.index(guess)]
        print("↑" if ans_lat_letter-guess_lat_letter else "↓")

    # d) Check for the Longitude
    print("3. Longitude")
    if long[names.index(guess)] == long[j]:
        print("✓")
    else:
        ans_long_letter = lat[j]
        guess_long_letter = lat[names.index(guess)]
        print("←" if ans_long_letter-guess_long_letter else "→")

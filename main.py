# Academic Adventure Game
print("🌟 Welcome to the Academic Adventure Game at EvCC! 🌟")
playerName = input("What\'s your name, hello dear adventurer? ")

print(f"\nWelcome, {playerName}! Your journey begins now. Let's start by choosing your role in this academic adventure.")

# Character Selection
print("\nChoose your character:")
characters = {
    "1": "A Super Wizard - Skilled in spells and potions.",
    "2": "A Researcher - Expert in logic and experimentation.",
    "3": "The Mastermind - Master of construction and problem-solving.",
    "4": "A Physiatrist - Specialist in health and recovery."
}
for key, description in characters.items():
    print(f"{key} - {description}")

characterChoice = input("Enter the number of your chosen character: ")
if characterChoice in characters:
    chosenCharacter = characters[characterChoice].split(" - ")[0]
else:
    print("Invalid choice! Defaulting to Scientist.")
    chosenCharacter = "Scientist"

print(f"\nGreat choice, {playerName}! You are now a {chosenCharacter}.")

# Area of Interest Selection
print("\nNext, choose your area of interest to guide your studies:")
interests = {
    "1": "Computing and IT",
    "2": "Science",
    "3": "Engineering",
    "4": "Health Sciences"
}
for key, area in interests.items():
    print(f"{key} - {area}")

interestChoice = input("Enter the number corresponding to your area of interest: ")
if interestChoice in interests:
    userInterest = interests[interestChoice]
else:
    print("Invalid choice! Defaulting to Science.")
    userInterest = "Science"

print(f"\nFantastic! You've chosen {userInterest} as your area of interest.")

# Getting Started Steps
print("\nLet's walk through the steps to get started with your studies.")
steps = [
    "Step 1: Complete your application.",
    "Step 2: Apply for financial aid if needed.",
    "Step 3: Take the placement tests.",
    "Step 4: Register for classes.",
    "Step 5: Attend orientation."
]

for step in steps:
    input(f"{step} (Press Enter to continue)")

print("\nYou're all set with the starting steps! Now, let's look at some recommended courses.")

# Course Suggestions
print("\n📚 Recommended Courses Based on Your Interest:")
courseSuggestions = {
    "Computing and IT": "STEM 101, STEM 103, and an English course",
    "Science": "STEM 101, STEM 102, and a Math course",
    "Engineering": "STEM 101, ENGR 111, and a Math course",
    "Health Sciences": "STEM 101, STEM 102, and an English course"
}
suggestedCourses = courseSuggestions.get(userInterest, "STEM 101 and general elective courses")

print(f"Suggested courses for {userInterest}: {suggestedCourses}")
print(f"\nGood luck, {playerName}! As a {chosenCharacter}, may your academic journey be filled with knowledge and adventure!")

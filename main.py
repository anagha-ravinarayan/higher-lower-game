import random
import art
from game_data import data

print(art.logo)
print("\nWelcome to the Higher Lower game of Instagram followers!")
print("Note: This data is based on the account's followers as on the end of 2020.")

answer_is_right = True
score = 0
option1 = random.choice(data)

while answer_is_right:
  option2 = random.choice(data)

  if option1['follower_count'] > option2['follower_count']:
    correct_answer = 'a'
  else:
    correct_answer = 'b'
    
  print(f"\nCompare A: {option1['name']}, a {option1['description']}, from {option1['country']}.")
  print(f"\nAgainst B: {option2['name']}, a {option2['description']}, from {option2['country']}.")
  answer = input("\nWho do you think has more followers? Type 'A' or 'B': ").lower()
  print("------------------------------------------------------------")
  if not answer == correct_answer:
    answer_is_right = False
    print(f"Sorry, that's wrong. Final score: {score}")
  else:
    option1 = option2
    score += 1
    print(f"You're right! Current score: {score}.")
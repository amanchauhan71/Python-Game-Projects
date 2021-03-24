from art import logo , vs
from game_data import data
import random


def format_data(data):
    new_name = data['name']
    new_description = data['description']
    new_country = data['country']
    new_data = new_name + "," + " a " + new_description + "," + " from " + new_country
    return new_data

def choice_followers(A,B):
    follower_A = A['follower_count']
    follower_B = B['follower_count']

    if follower_A > follower_B:
        return 'a'
    else:
        return 'b'


def game():
    print(logo)
    random_data_for_A= random.choice(data)
    random_data_for_against_B= random.choice(data)

    game_should_continue = True
    score = 0
    while game_should_continue:
        print(f"You are right! Current score: {score}")
        print(f"Compare A: {format_data(random_data_for_A)}.")
        print(vs)
        print(f"Against B: {format_data(random_data_for_against_B)}.")

        choice = input("Who has more followers? Type 'A' or 'B':").lower()
        winner = choice_followers(random_data_for_A ,random_data_for_against_B)

        if choice == winner and winner =='a' :

            random_data_for_against_B = random.choice(data)
            score += 1
        elif choice == winner and winner =='b':

            random_data_for_A = random_data_for_against_B
            random_data_for_against_B = random.choice(data)
            score += 1
        else :
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

        while random_data_for_A == random_data_for_against_B :
            random_data_for_against_B = random.choice(data)

game()

import streamlit as st
import random

# Initialize session state variables
if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 10)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

# Title and instructions
st.title("Number Guessing Game")
st.write("I'm thinking of a number between 1 and 10. Can you guess what it is?")

# Input from the user
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

# Button to submit the guess
if st.button("Submit Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.random_number:
            st.write("Your guess is too low! Try again.")
        elif guess > st.session_state.random_number:
            st.write("Your guess is too high! Try again.")
        else:
            st.write(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True

# Restart the game
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 10)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.write("New game started! Guess a new number.")

# Display number of attempts
st.write(f"Number of attempts: {st.session_state.attempts}")
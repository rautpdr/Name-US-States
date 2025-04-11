# NAME US STATES

An interactive U.S. geography quiz built with Python and Turtle graphics. The user is prompted to guess all 50 U.S. states, and correctly guessed states are labeled directly on the map in their correct locations.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

This project is a fun and educational game that tests your knowledge of U.S. geography. It uses Turtle graphics to render a map and allows users to enter state names. Each correct answer is marked on the map in real time. The game continues until all 50 states are named or the user exits.

It’s a great demonstration of combining data handling with interactive graphics in Python.

## How it Works

1. **Start the Game**: Run the `main.py` file.
2. **Guess the State**: A popup input appears asking for the name of a U.S. state.
3. **Correct Guesses**: If the guess is valid, the state's name is written on the map at its correct location.
4. **Completion**: The game ends automatically when all 50 states have been guessed correctly.

## Technologies Used

- **Python**: Main language
- **Turtle Graphics**: For rendering the U.S. map and placing text labels
- **Pandas**: To read and manage state data from a CSV file
- **CSV Data**: Used to store and update guessed and remaining states

## Lessons Learned

- **Data Integration**: Learned to combine CSV data with interactive visuals
- **Event Loops**: Managed input within a continuous guessing loop
- **Coordinate Mapping**: Displayed text on exact `(x, y)` map locations
- **User Experience**: Designed intuitive and engaging interactions with Turtle

## Acknowledgements

Inspired by classic geography quizzes and built with Python Turtle. Special thanks to the 50_states.csv dataset for enabling accurate state placement and to the Python community for sharing helpful tips and resources.

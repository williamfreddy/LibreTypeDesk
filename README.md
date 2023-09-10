# Typing Speed Application Documentation

## Introduction

This document provides documentation for the Typing Speed Application implemented in Python using the Tkinter library. The application is designed to help users practice typing and measure their typing speed (in words per minute, or WPM) while also providing real-time feedback.

### Application Features

- **Dark Mode:** The application is designed with a dark mode user interface for better readability and aesthetics.
    
- **Navbar:** The navigation bar provides easy access to different sections of the application, including "Learn," "Practice," and "Compete."
    
- **Input Text Box:** Users can type in the provided text box, and the application measures their typing speed and highlights incorrectly typed words.
    
- **Display WPM:** The application displays the user's typing speed in WPM in real-time.
    
- **Paragraph Content:** Users are presented with random paragraphs to type, helping them practice typing various text.
    

## User Interface

### Dark Mode

The application utilizes a dark mode interface, enhancing the visual experience.

### Navbar

The navigation bar contains buttons for different sections of the application:

- "Learn": Provides access to learning resources.
- "Practice": Allows users to practice typing.
- "Compete": Engages users in competitive typing challenges.

### Input Text Box

- The input text box is where users can type the given paragraph.
- It is designed with a dark background for contrast and readability.
- The text box's text color changes to red or orange if typing speed is below specific thresholds (indicating slower typing).

### Display WPM

- The application displays the current typing speed in WPM (Words Per Minute).
- The WPM value is updated in real-time as the user types.
- The text color of the WPM display changes based on typing speed:
    - Below 30 WPM: Red
    - Between 30 and 60 WPM: Orange
    - Above 60 WPM: White

### Paragraph Content

- The application provides random paragraphs for users to practice typing.
- The paragraphs are wrapped within the application window for easy reading.
- If a word is typed incorrectly, it is highlighted in red.

## Typing Speed Calculation

- The application calculates WPM based on the number of words typed and elapsed time.
- The timer starts when the user begins typing.
- WPM is updated in real-time and displayed to the user.

## Usage

1. Run the application.
2. Choose a section from the navigation bar.
3. Start typing the presented paragraph in the input text box.
4. The application will measure and display your typing speed in WPM.
5. Incorrectly typed words will be highlighted in red.

## Dependencies

- Python 3.x
- Tkinter library (usually included with Python)

## Implementation

The application is implemented in Python using the Tkinter library for the graphical user interface (GUI).

## Acknowledgments

The application was developed as a typing practice tool to improve typing skills and increase typing speed. It provides a user-friendly interface and real-time feedback for an enhanced learning experience.

---

Feel free to customize and expand upon this documentation as needed for your use in Obsidian or any other note-taking tool.

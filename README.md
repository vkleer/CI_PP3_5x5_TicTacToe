# 5x5 Tic-Tac-Toe
(Developer: Vilayat Kleer)

![mockup-image.jpg]()

[View the live website](https://ci-pp3-5x5-tictactoe.herokuapp.com/)

## Table of Contents

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Website Owner Goals](#website-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [User Manual](#user-manual)
3. [Technical Design](#technical-design)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Tools](#tools)
5. [Features](#features)
6. [Testing](#validation)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
- Play a simple and fun game for two players
- Be able to create and log in to an account that keeps my score

### Website Owner Goals
- Creating a fun game with clear instructions and simple mechanics
- Provide clear feedback to the players so they never get stuck

## User Experience

### Target Audience
- People who like Tic-Tac-Toe
- People who want to play a simple and fun game
- Casual gamers

### User Requirements and Expectations
- A simple, fun game that anyone can play
- Clear options for each menu or interaction
- Clear feedback provided when necessary
- Providing a personal touch through unique usernames

### User Manual
<details><summary>Click here for the user manual</summary>
#### Log in menu
When users start the program, they land on the log in menu. Above the menu, and on every other 'page' of the program except for the actual game, an ASCII logo of the game is shown. Below the logo the user is presented with two options.
Operation: Input a numeric value and press the enter key.
1. Log in
2. Create new account

If the user at any point in the program or game enters a value that does not correspond to the options available, they will receive feedback of what they entered and are reminded of the available options.

#### Log in
If option 1 is selected from the log in menu, the users will be asked to enter the email addresses they used to create an account. It will first ask player 1 to enter their email address and the player 2. It doesn't matter who logs in first as a random player will get the first turn each game.

Each email address is validated, first by checking if it follows the format of 'name@email.com' and second by looking up the email address in the database (Google Sheets file). 
If the email address doesn't follow the correct format, users will be given feedback, e.g. 'It must have exactly one @-sign'. If they enter the correct format but the email address is not registered, they will be presented with two options.
Operation: Input a numeric value and press the enter key.
1. Try different email address
2. Create new account

If option 1 is selected, the log in process is repeated. If option 2 is chosen, users will be able to create a new account, described below.

#### Create new account
If option 2 is selected in either the log in menu or after a failed log in, users will be taken here. 

Player 1 will be asked to provide a username for their account, which is validated: The username has to be between 2 to 20 characters long can only contain letters and digits - no special characters are allowed. After the validation, the username will be compared to the existing usernames in the database (Google Sheets file) and if a match is found, the player will be informed and has to provide a new username.

Then, player 1 will be asked to provide an email address for their account, which is also validated: the emaill address has to follow the format of 'name@email.com'. After the validation, the email address will be compared to the existing email addresses in the database (Google Sheets file) and if a match is found, the player will be informed and has to provide a new email address.

After player 1 has created their account, player 2 will be presented with two options.
Operation: Input a numeric value and press the enter key.
1. Create new account
2. Already have an account, go to log in menu

</details>

## User Stories

### User
1. As a user, I want to be able to read the game instructions
2. As a user, I want to be able to create an account
3. As a user, I want to be able to log in with my account
4. As a user, I want to be able to log out when I'm done
5. As a user, I want to be able to quit the game
6. As a user, I want to know how many games I've won
7. As a user, I want to receive feedback during and after the game
8. As a user, I want to be informed if I provide wrong input in the game

### Site owner
9. As the website owner, I want the game to be fair and have a random player get the first turn on each game
10. As the website owner, I want to provide feedback to users when they provide invalid input
11. As the website owner, I want usernames and email addresses to be saved to a Google Sheets file
12. As the website owner, I want users to be able to decide if they want to create one or two accounts during the registration process

## Technical Design

### Flowchart

### Data Models

## Technologies Used

### Languages
- Python

### Tools
- Gitpod
- Github
- Git

### Libraries

## Built-in Libraries

## THird Party Libraries

## Features
The website has a total of x features:

### Feature
- Feature description

## Testing

### Python Validation

### Manual Testing

### Automated Testing

### Testing User Stories
1. As a user, I want to be able to play the game on different difficulty levels

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Feature name | Action  | Expected result | Works as expected |

<details><summary>Supporting Screenshots - User Story 1</summary>
    <img src="docs/user-story-testing/user-story-01.png">
</details>


## Bugs

| **Bug** | **Fix** |
|-------------|------------|
| Bug | Fix - [link to commit](link) |


## Deployment

### GitHub

This website was deployed using Github Pages with the following steps:

1. Go to your Github Repository
2. Navigate to the 'Settings' page
3. On the left hand menu under 'Code and automationo', click on 'Pages'
4. Under 'Source', click on the 'Branch' dropdown element and set it to your main branch (in my case, this branch is called 'main')
5. Click on 'Save'
6. Refresh the page and you will be provided with a link to your deployed Github Page.

If you want to fork this repository, follow these steps:

1. Go to the Github repository (https://github.com/vkleer/CI_PP1_TD)
2. Click on the 'Fork' button in the top right corner under the navigation bar

If you want to clone this repository, follow these steps:

1. Go to the Github repository (https://github.com/vkleer/CI_PP1_TD)
2. Click on the 'Code' button above the list of files
3. Select your preferred way of cloning, I recommend using the 'GitHub CLI' option
4. Under 'GitHub CLI', click on the copy button to copy the clone command
5. In you IDE, open Git Bash
6. Navigate to the working directory where you want to clone this directory
7. Paste in the clone command you copied and press the 'enter' key to create the clone

## Credits
Images that are not referenced below are created or owned by the developer.

## Acknowledgements
I would like to thank:
- My mentor Mo Shami for providing me with advice and guidance for this project
- My partner Lauren Baker for helping me with testing and finding multiple bugs
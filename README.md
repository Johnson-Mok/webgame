# webgame

## Build and Containerize the Web Game
To containerize and deploy the game on the web, you'll need to have **Docker Desktop** installed and running. If you'd like to debug the container during development, you can optionally install the **Docker extension** for additional debugging capabilities.

### Steps to Build the Container:
1. **Ensure Docker is Running**: Make sure Docker Desktop is up and running before proceeding.
2. **Make the `run.sh` Script Executable** (if necessary): If you encounter issues running the `run.sh` script, check if it's executable. You can make it executable by running the following command in your bash terminal:
```bash
chmod +x run.sh
```
3. **Build the Docker Container**: Once everything is set, you can build the container by executing the `run.sh` script: 
```bash
./run.sh
```

## Backlog
### Core
- [] Score Tracking - Live Score Updates: Keep track of the player’s score as they answer questions.
- [] Score Tracking - Improve Aesthetics of Final Score Display
- [] Question Randomization - Random Question Order: Shuffle the order of questions each time the quiz starts.

### Enhance User Engagement
- [] Feedback for Each Question - Improve Aesthetics of Instant Feedback: Show whether the selected answer is correct or incorrect immediately after a user submits.
- [] Feedback for Each Question - Explanation: Provide a brief explanation after each question about the correct answer, helping with learning.
- [] Progress Tracking - Progress Bar: Show a progress bar indicating how far the user is through the quiz (e.g., “Question 5 of 10”).
- [] Question Randomization - Randomized Options: Shuffle the multiple-choice options for each question to avoid memorization of answers.
- [] Visual and Audio Feedback - Visual Feedback: Use colors (e.g., green for correct, red for wrong) and animations to enhance the experience.
- [] Visual and Audio Feedback - Sound Effects: Add sound effects for correct or incorrect answers (optional, but can be fun).
- [] Score Tracking - Score History: Store and display scores from previous attempts.

### User Choice & Difficulty
- [] Multiple Quiz Modes - Quiz Categories: Offer different categories of quizzes (e.g., animals, history, general knowledge).
- [] Levels of Difficulty - Difficulty Levels: Allow users to select a difficulty level (e.g., easy, medium, hard), with different sets of questions or scoring systems.
- [] Timer - Countdown Timer: Add a timer for each question or for the entire quiz, encouraging quick answers.
- [] Timer - Display Time Left: Show how much time is left for the current question or overall quiz.
- [] Hints and Lifelines - Hint System: Add a hint option for each question that reveals a clue.
- [] Hints and Lifelines - 50/50 Lifeline: Allow users to remove two incorrect answers as a lifeline.
- [] Hints and Lifelines - Skip Question: Give players the option to skip a question but with a penalty on the score or time.

### Additional Features
- [] Leaderboard - Local Leaderboard: Store and display the highest scores achieved by players on the local machine.
- [] Leaderboard - Global Leaderboard: Integrate with a database or an external service to store and display global scores (optional).
- [] User Authentication and Profiles - User Login: Let users create accounts and log in to track their quiz performance over time.
- [] User Authentication and Profiles - Profile Customization: Allow users to customize their profile or avatar.
- [] Review Missed Questions - Review Incorrect Answers: Let users review the questions they answered incorrectly at the end of the quiz.
- [] Visual and Audio Feedback - Theme Customization: Allow users to customize the appearance of the quiz, such as dark/light mode or different color themes.

### Advanced Gamification
- [] Timer - Timed vs. Untimed Mode: Give users the option to play with or without a timer.
- [] Levels of Difficulty - Gradual Difficulty: Start with easy questions and increase the difficulty as the quiz progresses.
- [] Multiple Quiz Modes - Challenge Mode: Create a special mode where players are scored based on how quickly they answer.
- [] Multiple Quiz Modes - Practice Mode: Let users practice without time limits or scoring.

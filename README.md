# Quiz App

In this project, you'll build a custom quiz app using Flask.

## Quiz Apps

Quiz apps are really popular.

[Sporcle](https://www.sporcle.com/games/g/world?t=world), for instance, offers
tons of different types of quizzes, usually with a timer.

Have you ever taken a Buzzfeed-style Quiz? If you haven't (or even if you have),
take a look at [These Disney Channel And K-Pop Songs Have The Same Title — Which 
Do You Prefer?](https://www.buzzfeed.com/sagehaley/disney-channel-vs-kpop-songs). The quiz isn't really about knowing anything or getting the answer right, it's
about entertainment.

[Mentimeter](https://www.menti.com/) is a quiz app for education, and 
[SurveyMonkey](https://www.surveymonkey.com/) is a quiz app for
surveys for businesses.

In this project, you'll use what you've learned so far about web apps to make 
your own quiz app. You can pick any style - you don't have to follow the style 
any of these apps.

## Requirements

- Your application must use Flask
- Your application must render a quiz using a template
- Your application must allow users to answer questions using a form
- Your application must handle the response to the form, and show the user their
    results

## Starter Code

There is an app.py file that renders a (mostly) empty html template.

Run the app locally with `flask run`.

## Steps

1. Design your quiz. Brainstorm the topic and write down the questions you want
   to ask the user.
2. Write the logic to show your quiz, and run the app to test that your display
   code works.
3. Write your quiz as an HTML form. You can write it in HTML directly, or keep
   the questions in Python and use template variables.
4. Write the logic to handle form submissions, so that quiz-takers see results
   after they have submitted the form.

Be sure to test your app and ensure that any inputs that need to be validated
are checked. Users should not be able to trigger an application error by
entering invalid inputs in the quiz.

## Optional

- You may add styles to the quiz app pages
- You may use a CSS framework
- You may render questions from a fixed list in your code, or from a database

## Rubric

| Points | Criteria | Description |
|---|---|---|
| 20 pts | Application runs | - Application starts with `flask run`<br>- Loads the '/' route without errors |
| 20 pts | Routes | - App uses multiple routes <br>- GET and POST methods used appropriately|
| 20 pts | Templates and forms | - App uses different templates for different pages <br>- App correctly uses form attributes to control form submission|
| 20 pts | error handling | - App runs without errors<br>- Inputs are validated appropriately|
| 20 pts | logic for questions | - Quiz questions are scored appropriately <br>- User sees the results based on what they entered in the form|
| 10 pts | Code is styled well | - Indented properly<br>- Organized effectively<br>- Appropriately commented |
| **100** | **Total** | 110 possible points with the bonus, scored out of 100 |

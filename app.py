from flask import Flask, redirect, render_template, request, session

import random

# The correct answer to each question is stored as the first entry of each question key's tuple value.
MATH_QUESTIONS_AND_ANSWERS = {
    'What is the Highest Common Factor(HCF) of 10 and 15?': (5, 10, 15, 8),
    'What is the Least Common Multiple(LCM) of 2 and 4?': (4, 2, 5, 8),
    'What is the only even prime number?': (2, 5, 6, 11),
    'What is the cube root of 27?': (3, 9, 4, 8),
    'What is the intersection of the sets {1, 2, 3} and {5, 2, 4}?': ('{ 2 }', '{ 4 }', '{ 1 }', '{ 5 }'),
}

# The correct answer to each question is stored as the first entry of each question key's tuple value.
PYTHON_QUESTIONS_AND_ANSWERS = {
    'Which expression counts the number of characters in a string s?': ('len(s)', 's.length', 'length(s)', 's.len'),
    'If "school" holds the string value "Kibo School". What is the output of the expression school.split()[-1]?': ('School', 'Kibo', 'Kibo School', 'Raises Error'),
    'Which of the following is not a valid python identifier?': ('8variable', 'variable8', 'va_ri_able', '_variable'),
    'A python function can be passed as a regular variable': ('True', 'False'),
    'Who invented the Python programming language?': ('Guido Van Rossum', 'Bjarne Stroustrup', 'James Gosling', 'John Smith'),
}

app = Flask(__name__)
app.secret_key = 'a very secret key'    # Required for using sessions


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz/math/")
def math_quiz_get():
    """
    Renders the math quiz page

    The correct answer of each question is stored as the first entry of its accompanying tuple.
    Hence, when rendering questions, the correct answer for each question is first retrieved and stored as a
    session value. The answers are finally shuffled before rendering the questions.

    Each question is assigned a unique name math_<question_number>, where question number is the position of
    the question(starting from 1) depending on how the dictionary supplies them. These unique names are used
    to map answers returned by users to appropriate questions.
    """

    context = []
    math_answers = {}
    count = 1

    for question, answers in MATH_QUESTIONS_AND_ANSWERS.items():
        question_name = f'math_{count}'   # generate unique question name
        answers = list(answers)
        math_answers[question_name] = str(answers[0])   # retrieve correct answer to the question

        random.shuffle(answers)     # shuffle answers to reorder them
        context.append((question_name, question, answers))  # Add question and shuffled answers to rendering context
        count += 1

    session['math_answers'] = math_answers

    return render_template('math.html', questions=context)


@app.route('/quiz/math/', methods=['POST'])
def math_quiz_post():
    """Record score of the math quiz and redirect to Python quiz page."""
    submitted_results = request.form.to_dict()
    result = 0

    for question_name in submitted_results:
        if submitted_results[question_name] == session['math_answers'][question_name]:
            result += 1

    session.pop('math_answers')
    session['math_score'] = result

    return redirect('/quiz/python/')


@app.route("/quiz/python/")
def python_quiz_get():
    """
    Renders the Python quiz page

    The correct answer of each question is stored as the first entry of its accompanying tuple.
    Hence, when rendering questions, the correct answer for each question is first retrieved and stored as a
    session value. The answers are finally shuffled before rendering the questions.

    Each question is assigned a unique name math_<question_number>, where question number is the position of
    the question(starting from 1) depending on how the dictionary supplies them. These unique names are used
    to map answers returned by users to appropriate questions.
    """

    context = []
    python_answers = {}
    count = 1

    for question, answers in PYTHON_QUESTIONS_AND_ANSWERS.items():
        question_name = f'python_{count}'
        answers = list(answers)
        python_answers[question_name] = str(answers[0])

        random.shuffle(answers)
        context.append((question_name, question, answers))
        count += 1

    session['python_answers'] = python_answers

    return render_template('python.html', questions=context)


@app.route('/quiz/python/', methods=['POST'])
def python_quiz_post():
    """Record score of the Python quiz as a session object and redirect to the quiz results page."""
    submitted_results = request.form.to_dict()
    result = 0

    for question_name, submitted_answer in submitted_results.items():
        if submitted_answer == session['python_answers'][question_name]:
            result += 1

    session.pop('python_answers')
    session['python_score'] = result

    return redirect('/quiz/result/')


@app.route('/quiz/result/')
def quiz_result():
    """
    Compute and render quiz results.

    The scores for the math and python quiz are retrieved from their respective session objects. The total score
    for the quiz is then computed from these values.
    """
    math_score = session.pop('math_score', 0)
    python_score = session.pop('python_score', 0)

    total_score = math_score + python_score
    percentage_score = (total_score / 10) * 100

    return render_template(
        'quiz-result.html',
        python_score=python_score,
        math_score=math_score,
        percentage_score=percentage_score
    )

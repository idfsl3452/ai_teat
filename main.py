from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define a function to generate a list of random numbers
def generate_lottery_numbers():
    lottery_numbers = []
    for i in range(6):
        number = random.randint(1, 26)
        while number in lottery_numbers:
            number = random.randint(1, 26)
        lottery_numbers.append(number)
    return lottery_numbers

# Define a function to compare the user's numbers to the lottery numbers
def check_numbers(user_numbers, lottery_numbers):
    matching_numbers = set(user_numbers).intersection(set(lottery_numbers))
    matching_result = f"Winning numbers : {lottery_numbers} Your numbers : {user_numbers} "
    if len(matching_numbers) == 0:
        return matching_result + "Sorry, you didn't win this time."
    elif len(matching_numbers) == 1:
        return matching_result + "Congratulations! You matched 1 number and win a free ticket."
    elif len(matching_numbers) == 2:
        return matching_result + "Congratulations! You matched 2 numbers and win a free ticket."
    elif len(matching_numbers) == 3:
        return matching_result + "Congratulations! You matched 3 numbers and win a free ticket."
    elif len(matching_numbers) == 4:
        return matching_result + "Congratulations! You matched 4 numbers and win $100."
    elif len(matching_numbers) == 5:
        return matching_result + "Congratulations! You matched 5 numbers and win $10,000."
    else:
        return "Congratulations! You matched all 6 numbers and win the jackpot!"

# Define a route to render the form
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle the form submission
@app.route('/check_numbers', methods=['POST'])
def check():
    # Generate the lottery numbers
    lottery_numbers = generate_lottery_numbers()

    # Get the user's numbers from the form
    user_numbers = [int(number) for number in request.form.getlist('numbers[]')]

    # Check the user's numbers against the lottery numbers
    result = check_numbers(user_numbers, lottery_numbers)

    # Render the result template with the result
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
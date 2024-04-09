from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

exchange_rates = {
    ('USD', 'EUR'): 0.85,
    ('EUR', 'USD'): 1.18,
    ('USD', 'GBP'): 0.72,
    ('GBP', 'USD'): 1.39,
    ('USD', 'INR'): 83.3,
    ('INR', 'USD'): 0.012,
}

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Get busy living or get busy dying. – Stephen King",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "The purpose of our lives is to be happy. – Dalai Lama",
    "You miss 100% of the shots you don't take. – Wayne Gretzky",
    "In the end, it's not the years in your life that count. It's the life in your years. – Abraham Lincoln",
    "You know you're in love when you can't fall asleep because reality is finally better than your dreams. – Dr. Seuss",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. – Jordan Belfort",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. – Steve Jobs",
    "Don't cry because it's over, smile because it happened. – Dr. Seuss",
    "You can never cross the ocean until you have the courage to lose sight of the shore. – Christopher Columbus",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. – Nelson Mandela",
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "If you want to lift yourself up, lift up someone else. – Booker T. Washington",
    "Life is either a daring adventure or nothing at all. – Helen Keller",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It is during our darkest moments that we must focus to see the light. - Aristotle",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Change your thoughts and you change your world. - Norman Vincent Peale",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
    "The only person you should try to be better than is the person you were yesterday. - Anonymous",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The two most important days in your life are the day you are born and the day you find out why. - Mark Twain",
    "Everything you've ever wanted is on the other side of fear. - George Addair",
    "The only source of knowledge is experience. - Albert Einstein",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The mind is everything. What you think you become. - Buddha",
    "The best revenge is massive success. - Frank Sinatra",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "If you can't explain it simply, you don't understand it well enough. - Albert Einstein",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "What we think, we become. - Buddha",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "In the end, it's not the years in your life that count. It's the life in your years. - Bodhai Man",
]

recipes = [
    {"id": 1, "title": "Rice Pudding", "ingredients": ["rice", "milk", "sugar"]},
    {"id": 2, "title": "Banana Bread", "ingredients": ["banana", "flour", "sugar", "eggs"]},
    {"id": 3, "title": "Apple Pie", "ingredients": ["apple", "flour", "sugar", "butter"]},
    {"id": 4, "title": "Wheat Pancakes", "ingredients": ["wheat flour", "milk", "eggs", "butter"]},
]

@app.route('/exchange-rates')
def get_exchange_rate():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')

    if from_currency is None or to_currency is None:
        return jsonify({'error': 'Both "from" and "to" parameters are required'}), 400

    try:
        rate = exchange_rates[(from_currency, to_currency)]
        return jsonify({'from': from_currency, 'to': to_currency, 'rate': rate})
    except KeyError:
        return jsonify({'error': 'Exchange rate not found for the specified currency pair'}), 404

@app.route('/quotes/random')
def get_random_quote():
    random_quote = random.choice(quotes)
    return jsonify({'quote': random_quote})

@app.route('/recipes')
def search_recipes():
    ingredient = request.args.get('ingredient')
    if not ingredient:
        return jsonify({'error': 'No ingredient provided'}), 400
    
    matching_recipes = [recipe for recipe in recipes if ingredient.lower() in [ing.lower() for ing in recipe['ingredients']]]
    if not matching_recipes:
        return jsonify({'error': 'No recipes found for the provided ingredient'}), 404
    
    return jsonify(matching_recipes)

@app.route('/weather')
def get_random_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'No city provided'}), 400
    
    temperature = round(random.uniform(-20, 40), 1) 
    humidity = random.randint(0, 100) 
    conditions = ['Sunny', 'Cloudy', 'Rainy', 'Snowy']
    condition = random.choice(conditions)  
    
    return jsonify({
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'condition': condition
    })



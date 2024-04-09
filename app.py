from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

exchange_rates = {
    ('USD', 'USD'): 1,
    ('USD', 'GBP'): 0.8800,
    ('USD', 'EUR'): 1.1400,
    ('USD', 'INR'): 70.9800,
    ('USD', 'SAR'): 3.7500,
    ('USD', 'AED'): 3.6700,
    ('EUR', 'EUR'): 1,
    ('EUR', 'GBP'): 0.7200,
    ('EUR', 'USD'): 1.3900,
    ('EUR', 'INR'): 83.3000,
    ('EUR', 'SAR'): 3.7500,
    ('EUR', 'AED'): 3.6700,
    ('GBP', 'GBP'): 1,
    ('GBP', 'USD'): 1.1800,
    ('GBP', 'EUR'): 0.0140,
    ('GBP', 'INR'): 70.9800,
    ('GBP', 'SAR'): 3.7500,
    ('GBP', 'AED'): 3.6700,
    ('INR', 'INR'): 1,
    ('INR', 'USD'): 0.0120,
    ('INR', 'GBP'): 0.8800,
    ('INR', 'EUR'): 1.1400,
    ('INR', 'SAR'): 3.7500,
    ('INR', 'AED'): 3.6700,
    ('SAR', 'SAR'): 1,
    ('SAR', 'USD'): 1.1800,
    ('SAR', 'GBP'): 0.8800,
    ('SAR', 'EUR'): 1.1400,
    ('SAR', 'INR'): 70.9800,
    ('SAR', 'AED'): 3.6700,
    ('AED', 'AED'): 1,
    ('AED', 'USD'): 1.1800,
    ('AED', 'GBP'): 0.8800,
    ('AED', 'EUR'): 1.1400,
    ('AED', 'INR'): 70.9800,
    ('AED', 'SAR'): 3.7500,
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
    {
      "id": 5,
      "title": "Creamy Tomato Pasta",
      "ingredients": ["pasta", "tomatoes", "garlic", "olive oil", "heavy cream", "parmesan cheese"]
  },
  {
      "id": 6,
      "title": "Cheesy Chicken Enchiladas",
      "ingredients": ["chicken breast", "tortillas", "cheese", "enchilada sauce", "onion", "cumin", "chili powder"]
  },
  {
      "id": 7,
      "title": "Stir-Fried Vegetables with Tofu",
      "ingredients": ["tofu", "broccoli", "red bell pepper", "soy sauce", "sesame oil", "ginger", "rice"]
  },
  {
      "id": 8,
      "title": "Black Bean Burgers",
      "ingredients": ["black beans", "brown rice", "corn", "breadcrumbs", "onion", "cumin", "paprika"]
  },
  {
      "id": 9,
      "title": "Lentil Soup",
      "ingredients": ["lentils", "carrots", "celery", "onion", "chicken broth", "cumin", "turmeric"]
  },
  {
      "id": 10,
      "title": "Chocolate Chip Cookies",
      "ingredients": ["butter", "sugar", "eggs", "flour", "chocolate chips", "vanilla extract"]
  },
  {
      "id": 11,
      "title": "Salmon with Roasted Vegetables",
      "ingredients": ["salmon fillet", "broccoli", "asparagus", "olive oil", "lemon juice", "salt", "pepper"]
  },
  {
      "id": 12,
      "title": "Chicken Caesar Salad",
      "ingredients": ["romaine lettuce", "grilled chicken", "parmesan cheese", "croutons", "Caesar dressing"]
  },
  {
      "id": 13,
      "title": "Beef Tacos",
      "ingredients": ["ground beef", "taco shells", "shredded cheese", "lettuce", "tomato", "onion", "taco seasoning"]
  },
  {
      "id": 14,
      "title": "Cream of Broccoli Soup",
      "ingredients": ["broccoli florets", "chicken broth", "onion", "garlic", "heavy cream", "milk", "cheese"]
  },
  {
      "id": 15,
      "title": "Thai Curry with Vegetables",
      "ingredients": ["coconut milk", "curry paste", "red bell pepper", "zucchini", "snow peas", "basil leaves", "rice"]
  },
  {
      "id": 16,
      "title": "Quinoa Salad with Berries",
      "ingredients": ["quinoa", "mixed berries", "spinach", "feta cheese", "almonds", "honey balsamic dressing"]
  },
  {
      "id": 17,
      "title": "Tuna Noodle Casserole",
      "ingredients": ["canned tuna", "egg noodles", "cream of mushroom soup", "peas", "bread crumbs", "milk"]
  },
  {
      "id": 18,
      "title": "Vegetable Spring Rolls",
      "ingredients": ["spring roll wrappers", "shredded cabbage", "carrots", "green onions", "tofu (optional)", "soy sauce", "rice vinegar", "sesame oil"]
  },
  {
      "id": 19,
      "title": "Chicken Pot Pie",
      "ingredients": ["pie crust dough", "chicken breast", "carrots", "celery", "peas", "chicken broth", "heavy cream", "mixed herbs"]
  },
  {
      "id": 20,
      "title": "Pumpkin Muffins",
      "ingredients": ["pumpkin puree", "eggs", "sugar", "flour", "baking powder", "cinnamon", "nutmeg", "pumpkin seeds (optional)"]
  },
   {
      "id": 21,
      "title": "French Toast",
      "ingredients": ["bread slices", "eggs", "milk", "cinnamon", "vanilla extract", "butter", "maple syrup (optional)"]
  },
  {
      "id": 22,
      "title": "Scrambled Eggs with Smoked Salmon",
      "ingredients": ["eggs", "smoked salmon", "butter", "chives", "salt", "pepper"]
  },
  {
      "id": 23,
      "title": "Chicken Stir-Fry with Noodles",
      "ingredients": ["chicken breast", "rice noodles", "broccoli", "carrots", "soy sauce", "rice vinegar", "sesame oil", "ginger"]
  },
  {
      "id": 24,
      "title": "Lentil Shepherd's Pie",
      "ingredients": ["lentils", "brown lentils", "vegetables (corn, peas, carrots)", "mashed potatoes", "onion", "garlic", "thyme", "vegetable broth"]
  },
  {
      "id": 25,
      "title": "Black Bean Soup with Avocado Crema",
      "ingredients": ["black beans", "chicken broth", "corn", "tomatoes", "onion", "cumin", "chili powder", "avocado", "lime juice", "cilantro"]
  },
  {
      "id": 26,
      "title": "Baked Salmon with Lemon Herb Butter",
      "ingredients": ["salmon fillet", "lemon", "butter", "fresh herbs (parsley, dill)", "garlic", "salt", "pepper"]
  },
  {
      "id": 27,
      "title": "Chicken Fajitas",
      "ingredients": ["chicken breast strips", "bell peppers (various colors)", "onion", "fajita seasoning", "tortillas", "shredded cheese", "guacamole (optional)", "salsa (optional)"]
  },
  {
      "id": 28,
      "title": "One-Pot Pasta Primavera",
      "ingredients": ["pasta (penne, farfalle)", "cherry tomatoes", "zucchini", "peas", "garlic", "olive oil", "parmesan cheese", "fresh basil"]
  },
  {
      "id": 29,
      "title": "Creamy Tomato Bisque",
      "ingredients": ["tomatoes", "onion", "garlic", "heavy cream", "chicken broth", "thyme", "bay leaf", "salt", "pepper"]
  },
  {
      "id": 30,
      "title": "Chocolate Mug Cake",
      "ingredients": ["flour", "cocoa powder", "sugar", "baking powder", "milk", "oil", "chocolate chips (optional)"]
  },
   {
      "id": 31,
      "title": "Beef and Broccoli",
      "ingredients": ["flank steak", "broccoli florets", "soy sauce", "brown sugar", "rice vinegar", "cornstarch", "water", "ginger", "garlic", "rice"]
  },
  {
      "id": 32,
      "title": "Chicken and Vegetable Stir-Fry with Cashew Nuts",
      "ingredients": ["chicken breast", "assorted vegetables (broccoli, carrots, snap peas)", "cashew nuts", "soy sauce", "honey", "rice vinegar", "sesame oil", "ginger", "garlic", "rice"]
  },
  {
      "id": 33,
      "title": "Spiced Chickpea Curry",
      "ingredients": ["chickpeas", "coconut milk", "curry powder", "tomatoes", "onion", "garam masala", "ginger", "cilantro", "rice"]
  },
  {
      "id": 34,
      "title": "Caprese Salad",
      "ingredients": ["fresh mozzarella cheese", "tomatoes", "fresh basil leaves", "olive oil", "balsamic vinegar", "salt", "pepper"]
  },
  {
      "id": 35,
      "title": "Chicken Caesar Wraps",
      "ingredients": ["romaine lettuce leaves", "grilled chicken breast slices", "Caesar dressing", "parmesan cheese", "croutons (optional)"]
  },
  {
      "id": 36,
      "title": "Beef Stroganoff",
      "ingredients": ["beef sirloin", "mushrooms", "onion", "beef broth", "sour cream", "Dijon mustard", "egg noodles"]
  },
  {
      "id": 37,
      "title": "Chicken Noodle Soup",
      "ingredients": ["chicken breast", "egg noodles", "carrots", "celery", "onion", "chicken broth", "parsley"]
  },
  {
      "id": 38,
      "title": "Tuna Salad Sandwiches",
      "ingredients": ["canned tuna", "mayonnaise", "celery", "red onion", "dill", "bread slices"]
  },
  {
      "id": 39,
      "title": "Cheesy Potato Soup",
      "ingredients": ["potatoes", "chicken broth", "onion", "garlic", "heavy cream", "milk", "cheddar cheese", "paprika"]
  },
  {
      "id": 40,
      "title": "Greek Yogurt Parfait with Berries and Granola",
      "ingredients": ["greek yogurt", "mixed berries", "granola", "honey (optional)"]
  },
  {
      "id": 41,
      "title": "Chicken Enchiladas with Green Chile Sauce",
      "ingredients": ["chicken breast", "tortillas", "green chile sauce", "cheese", "onion", "cumin", "chili powder"]
  },
  {
      "id": 42,
      "title": "Shrimp Scampi",
      "ingredients": ["shrimp", "butter", "garlic", "white wine", "lemon juice", "parsley", "pasta"]
  },
  {
      "id": 43,
      "title": "Turkey Chili",
      "ingredients": ["ground turkey", "kidney beans", "black beans", "corn", "diced tomatoes", "chili powder", "cumin", "onion", "chicken broth"]
  },
  {
      "id": 44,
      "title": "Chicken Pot Pie with Puff Pastry Crust",
      "ingredients": ["chicken breast", "carrots", "celery", "peas", "chicken broth", "heavy cream", "mixed herbs", "puff pastry dough"]
  },
  {
      "id": 45,
      "title": "Beef Tacos with Guacamole",
      "ingredients": ["ground beef", "taco shells", "shredded cheese", "lettuce", "tomato", "onion", "taco seasoning", "avocados", "lime juice", "cilantro (for guacamole)"]
  },
  {
      "id": 46,
      "title": "Chicken Fajita Quesadillas",
      "ingredients": ["chicken breast strips", "bell peppers (various colors)", "onion", "fajita seasoning", "tortillas", "shredded cheese"]
  },
  {
        "id": 47,
        "title": "Lemon Ricotta Pancakes",
        "ingredients": ["flour", "sugar", "baking powder", "salt", "eggs", "milk", "ricotta cheese", "lemon zest", "butter", "maple syrup (optional)"]
    },
    {
        "id": 48,
        "title": "Black Bean Burgers with Sweet Potato Fries",
        "ingredients": ["black beans", "brown rice", "corn", "breadcrumbs", "onion", "cumin", "paprika", "sweet potatoes", "olive oil", "salt", "pepper"]
    },
    {
        "id": 49,
        "title": "Creamy Tomato Tortilla Soup",
        "ingredients": ["tomatoes", "chicken broth", "onion", "garlic", "cumin", "chili powder", "canned corn (optional)", "cream cheese", "tortilla strips", "avocado (optional)", "cilantro (optional)"]
    },
    {
        "id": 50,
        "title": "Stir-Fried Tofu with Vegetables and Peanut Sauce",
        "ingredients": ["tofu", "broccoli florets", "red bell pepper", "snow peas", "soy sauce", "rice vinegar", "sesame oil", "ginger", "peanut butter", "rice"]
    }
]

print(recipes)

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
    
    matching_recipes = [recipe for recipe in recipes if ingredient.lower() in [ing.lower().split() for ing in recipe['ingredients']]]
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



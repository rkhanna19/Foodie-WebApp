from flask import Flask, render_template
from image_bot import ImageBot
from time import sleep

app = Flask(__name__)

foods = [
    {
        'name' : "Chicken Tikka Masala",
        'description' : "Chicken tikka masala is a dish of chunks of roasted marinated chicken in a spiced curry sauce.",
        'chef' : ""
    },
    {
        'name' : "Butter Chicken",
        'description' : "Butter chicken or makhan murg is a dish, originating in the Indian subcontinent, of chicken in a mildly spiced tomato sauce.",
        'chef' : "Rajesh Khanna"
    },
    {
        'name' : "Paneer Tikka",
        'description' : "Paneer tikka is an Indian dish made from chunks of paneer marinated in spices and grilled in a tandoor.",
        'chef' : "Rajesh Khanna"
    }
]

bot = ImageBot()
for food in foods:
    image_url = bot.find_image(food['name'])
    food['image'] = image_url
    sleep(0.3)

bot.kill()

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', foods=foods, user="Rajit")

@app.route('/about')
def about():
    return render_template('about.html', user="Rajit")

if __name__ == '__main__':
    app.run(debug=True)

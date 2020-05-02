from flask import Flask, render_template, url_for
from image_bot import ImageBot
from time import sleep

app = Flask(__name__)

foods = [
    {
        'name': 'Chicken Tikka Masala',
        'description': 'Chicken tikka masala is a dish of chunks of roasted marinated chicken in a spiced curry sauce.',
        'chef': '',
        'image': 'https://cafedelites.com/wp-content/uploads/2018/04/Best-Chicken-Tikka-Masala-IMAGE-2.jpg'
    },
    {
        'name': 'Butter Chicken',
        'description': 'Butter chicken or makhan murg is a dish, originating in the Indian subcontinent, of chicken in a mildly spiced tomato sauce.',
        'chef': 'Rajesh Khanna',
        'image': 'https://cafedelites.com/wp-content/uploads/2019/01/Butter-Chicken-IMAGE-64.jpg'
    },
    {
        'name': 'Paneer Tikka',
        'description': 'Paneer tikka is an Indian dish made from chunks of paneer marinated in spices and grilled in a tandoor.',
        'chef': 'Rajesh Khanna',
        'image': 'https://www.cookwithmanali.com/wp-content/uploads/2015/07/Restaurant-Style-Recipe-Paneer-Tikka.jpg'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', foods=foods, user="Rajit")

@app.route('/about')
def about():
    return render_template('about.html', user="Rajit")

if __name__ == '__main__':
    if 'image' not in foods[0]:
        bot = ImageBot()
        for food in foods:
            image_url = bot.find_image(food['name'])
            food['image'] = image_url
            bot.reset()
            sleep(0.3)

        bot.kill()
    app.run(debug=True)

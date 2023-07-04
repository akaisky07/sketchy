from flask import Flask, render_template
import os
import random
app = Flask(__name__)

@app.route('/')
def index():
    # Get a list of all PNG files in the "static" folder
    img_files = [f for f in os.listdir('static') if f.endswith('.png')]

    # Select a random file from the list
    random_img = random.choice(img_files)

    # Render the "index.html" template, passing in the random image file name
    return render_template('index.html', img_file=random_img)

if __name__ == '__main__':
    app.run(debug=True)


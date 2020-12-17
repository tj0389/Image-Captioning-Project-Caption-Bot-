from flask import Flask, request, jsonify, render_template
from static.model import caption_it
import os

app = Flask(__name__)

UPLOAD_FOLDER = './static/images'

@app.route('/')
def home():
    return render_template('index.html',user_image='./static/images/'+'1.jpg')

@app.route('/upload',methods=['POST'])
def upload():
    try:
        
        # check if the post request has the file part
        file = request.files['myImage']
        path='./static/images/{}'.format(file.filename)
        file.save(path)
        
        caption=caption_it.get_caption(path)

        return render_template('index.html', status=caption,user_image=path)

    except Exception as err:
        print("Error occurred")
        return render_template('index.html', status=err)

    
if __name__ == "__main__":
    app.run(debug=True)
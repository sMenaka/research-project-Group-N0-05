from flask import Flask, request, flash
import model as model
import os
from flask_cors import CORS

app = Flask(__name__)
@app.route('/')
def index():
	return ""

if __name__ == '__main__':
	app.run(debug=True)


UPLOAD_FOLDER = '../source'
ALLOWED_EXTENSIONS = set(['wav'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    streesCount=0
    notCount=0
    if request.method == 'POST':
        file = request.files["file"]
        pathname = os.path.join("source", file.filename)
        file.save(pathname)
        print(file)
        os.system("rm -rf source/decoded.wav")
        os.system("ffmpeg -i source/test.mp3 -vn -acodec pcm_s16le -ac 1 -ar 44100 -f wav source/decoded.wav")
        prds=model.predict("source/decoded.wav")
        print("pred len {} ".format(len(prds)))
        for i in prds:
            if i == 0:
                notCount+=1
            else:
                streesCount+=1
        print("not {} ".format(notCount))
        print("Stress {} ".format(streesCount))
        if notCount > streesCount:
            return "Not stress"
        else:
            return "Stress"
    
            
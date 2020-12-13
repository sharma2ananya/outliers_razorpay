from main import Run
from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER


# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      print(uploaded_file)
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           run = Run(file_path)
           result = run.update_sheet()
           print(result)
      return redirect(url_for('index'))

def parseCSV(file_path):
    csvData = pd.read_csv(file_path,names = col_names, header = None)
    for i in csvData.iterrows():
        print(i)


if (__name__ == "__main__"):
     app.run(port = 5000)
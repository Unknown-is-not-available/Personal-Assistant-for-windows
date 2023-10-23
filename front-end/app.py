from flask import Flask, request, jsonify
from flask_cors import CORS
#import gglsrch
import webbrowser

app = Flask(__name__)
CORS(app) 
@app.route('/',methods=['POST'])
def index():
    try:
        exec(open("gglsrch.py").read())
        return jsonify({"message":"successfully ran"})
    except Exception as e:
        print(e)
        return jsonify({"message":"not successfully ran"})
    
    
    #data = request.get_json()  #{ text: writin }
    #received_text = data['text']
    # Process the received text as needed
    #print("Received text:", received_text)
    # You can perform further processing with the text here
    #return jsonify({"message": "Text received successfully"})

if __name__ == '__main__':
    app.run(debug=True)
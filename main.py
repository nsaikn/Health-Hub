from flask import Flask
app = Flask("Food Manager")

tasks = [
    {
        'id': 1,
        'title': u'Display list',
        'description': u'chips, Cheese, Pizza, apple', 
        'done': False
    },
  
]

@app.route('/page1/food_list', methods=['GET'])
def get_list():
    return jsonify({'tasks': tasks})


@app.route("/")
def hello():
    myFile = open("heading1.html")
    pageContents = myFile.read()
    myFile.close()
    
    return pageContents

    

#@app.route("/page1") #Food
    

#@app.route("/page2") #log_Trigger


#@app.route("/page3") #Trigger


if __name__ == "__main__":
    app.run()


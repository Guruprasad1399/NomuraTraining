from flask import Flask, jsonify, render_template

app= Flask(__name__)

@app.route('/')
def api_index():
    return jsonify({"message": "Welcome to the API!","response":"Welcome to the API!"}),200

@app.route('/docs')
def api_docs():
    return render_template("docs.html",context={"message": "Welcome to the API Documentation"})

if __name__ == '__main__':
    app.run(debug=True,port=5001,host='0.0.0.0')
from flask import Flask, request, jsonify 
from summarizer import summarize_text 

from generator import generate_blog
 
app = Flask(__name__) 
 
@app.route("/summarize", methods=["POST"]) 
def summarize(): 
 
    data = request.json 
 
    result = summarize_text( 
        data["text"] 
    ) 
 
    return jsonify({ 
        "summary": result 
    }) 

from flask import request, jsonify
 
@app.route("/blog", methods=["POST"])
def blog_generator():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    topic = data.get("topic", "")
    
    if not topic:
        return jsonify({"error": "topic is required"}), 400

    result = generate_blog(topic)
    return jsonify({"blog": result})

if __name__ == "__main__": 
    app.run(debug=True) 
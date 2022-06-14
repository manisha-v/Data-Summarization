from flask import Flask, render_template, redirect,request,url_for
import requests

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods = ['GET','POST'])
def summarize():
    if request.method == 'POST':
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}

        data = request.form["data"]
        max = int(request.form["max"])
        min = max//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": data,
            "parameters": {"min_length": min, "max_length": max}
        })[0]
        return render_template("index.html", result = output["summary_text"])
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)

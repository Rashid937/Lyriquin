from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

# Vercel requires a specific handler for Serverless Functions
def handler(request, *args):
    return app(request.environ, start_response)

if __name__ == '__main__':
    app.run()

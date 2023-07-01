from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/clothes/')
def clothes_page():
    return render_template("clothes.html")


@app.route('/shoes/')
def shoes_page():
    return render_template("shoes.html")


@app.route('/jacket/')
def jacket_page():
    return render_template("jacket.html")

if __name__ == "__main__":
    app.run()
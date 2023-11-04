from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu():
    # menu.htmlテンプレートをレンダリングし、メニューデータを渡す
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    # return "ping-pong"
    games = [ "Jungel-Speed", "Katan", "Chest", "Damka", "Cheat", "Cambio", "Shesh-Besh"]
    return render_template("index.html",
    	likes_same_sport = True,
    	games=games)



if __name__ == '__main__':
   app.run(debug = True)


render_template(index.html)
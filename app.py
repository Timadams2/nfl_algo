import json
import requests
import http.client
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BET_FILE = "bets.json"

def load_bets():
    try:
        with open(BET_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_bet(bet):
    bets = load_bets()
    bets.append(bet)
    with open(BET_FILE, "w") as f:
        json.dump(bets, f, indent=4)


# -----------------------------
# MAIN DASHBOARD
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    bets = load_bets()
    return render_template("index.html", result=bets)


# -----------------------------
# ADD BET (form POSTs here)
# -----------------------------
@app.route("/add-bet", methods=["POST"])
def add_bet():
    bet = {
        "team": request.form.get("team"),
        "amount": request.form.get("amount"),
        "type": request.form.get("type"),
        "spread": request.form.get("spread"),
        "total": request.form.get("total"),
        "date": request.form.get("date"),
        "open": request.form.get("open")
    }

    save_bet(bet)
    return redirect(url_for("index"))

@app.route("/slate")
def slate():
    conn = "https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=0b131ba84bc49fe93d4b7aff87108e89&regions=us&markets=h2h,spreads&oddsFormat=american"
    response = requests.get(conn).json()
    print(response)

    return render_template("slate.html", games=response)

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/algos")
def algos():
    return render_template("algos.html")

if __name__ == "__main__":
    app.run(debug=True)

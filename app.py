import json
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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        team_a = request.form.get("team_a")
        team_b = request.form.get("team_b")

        result = f"Simulated matchup: {team_a} vs {team_b}"
        return render_template("results.html", result=result)

    return render_template("index.html")

@app.route("/add-bet", methods=["GET", "POST"])
def add_bet():
    if request.method == "POST":
        bet = {
            "team": request.form.get("team"),
            "amount": request.form.get("amount"),
            "type": request.form.get("type")
        }
        save_bet(bet)
        return redirect(url_for("view_bets"))

    return render_template("add_bet.html")

@app.route("/bets")
def view_bets():
    bets = load_bets()
    return render_template("results.html", result=bets)

if __name__ == "__main__":
    app.run(debug=True)

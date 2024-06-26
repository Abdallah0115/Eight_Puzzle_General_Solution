from flask import Flask, render_template, request
from the_game import game

ePuzzle = Flask(__name__)

@ePuzzle.route("/")
def homePage():
    return render_template("base.html")

@ePuzzle.route("/solution/",methods = ["POST"])
def Soln():
    initial = [
        [request.form.get('I1'),request.form.get('I2'),request.form.get('I3')],
        [request.form.get('I4'),request.form.get('I5'),request.form.get('I6')],
        [request.form.get('I7'),request.form.get('I8'),request.form.get('I9')]
    ]

    goal = [
        [request.form.get('g1'),request.form.get('g2'),request.form.get('g3')],
        [request.form.get('g4'),request.form.get('g5'),request.form.get('g6')],
        [request.form.get('g7'),request.form.get('g8'),request.form.get('g9')]
    ]

    heuri = 1 if request.form.get('flexRadioDefault') == "Missblaced" else 0

    E_P = game

    sol = E_P.game_puzzle(E_P,initial,goal,heuri)

    moves = E_P.moves(E_P,sol)
    sol = [x.state_r() for x in sol]

    return render_template("soln.html",**{"items":sol,"moves" :moves})

if __name__ == "__main__":
    ePuzzle.run(debug=True)
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from wrapper import SpadesWeb

"""literally just following the flask tutorial here just to see i can do with it"""

DEBUG = True
SECRET_KEY = 'herf'
CSRF_ENABLED = True

app = Flask(__name__)

"""Grabs globals etc from this file"""
app.config.from_object(__name__)


@app.route('/')
def show_home():
  return render_template('enter_users.html')


@app.route('/init', methods=['POST'])
def select_users():
  users = int(request.form['num_of_users'])

  if 0 < users and users <= 4:
    app.game = SpadesWeb(users, 52 / (users + 1))
  else:
    flash('Please enter a player count of one through four')
    return redirect(url_for('show_home'))
  return redirect(url_for('show_table'))


@app.route('/table', methods=['POST', 'GET'])
def show_table():
   return render_template('table.html', hand=app.game.players[0].hand)


@app.route('/play_card', methods=['POST'])
def play_card():
  cardIndex = int(request.form['card_index'])
  #app.game.


if __name__ == '__main__':
  app.run()

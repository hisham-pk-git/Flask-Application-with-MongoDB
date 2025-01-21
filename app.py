from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb+srv://hisham-pk:hismongo@hisham.j4b8v.mongodb.net/')
db = client.note_app
notes_collection = db.notes

@app.route('/')
def home():
    notes = list(notes_collection.find())
    return render_template('home.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note_text = request.form.get('note')
    cwid = request.form.get('cwid')
    full_name = request.form.get('full_name')
    if note_text and cwid and full_name:
        notes_collection.insert_one({'note': note_text, 'cwid': cwid, 'full_name': full_name})
    return redirect(url_for('home'))


@app.route('/delete/<note_id>', methods=['POST'])
def delete_note(note_id):
    notes_collection.delete_one({'_id': ObjectId(note_id)})
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)






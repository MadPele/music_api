import os

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


@app.route('/')
def test_get():
    info = requests.get('http://localhost:5000/')
    return render_template('home.html', data=info.json())


@app.route('/add', methods=['POST', 'GET'])
def test_post():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        artist = request.form['artist']
        album = request.form['album']
        track = request.form['track']
        duration_min = request.form['duration_min']
        duration_sec = request.form['duration_sec']
        if len(duration_sec) == 1:
            duration_sec = '0' + duration_sec
        track_format = request.form['format']
        year = request.form['year']
        command = f'curl -X POST --data "artist={artist}&album={album}&track={track}&' \
                  f'duration={duration_min}:{duration_sec}&format={track_format}&year={year}" http://127.0.0.1:5000/'
        os.system(command)
        return redirect(url_for('test_get'))


@app.route('/update', methods=['POST', 'GET'])
def test_update():
    if request.method == 'GET':
        return render_template('update.html')
    elif request.method == 'POST':
        artist = request.form['artist']
        album = request.form['album']
        track = request.form['track']
        up_title = request.form['up_title']
        up_duration_min = request.form['up_duration_min']
        up_duration_sec = request.form['up_duration_sec']
        if len(up_duration_sec) == 1:
            up_duration_sec = '0' + up_duration_sec
        up_format = request.form['up_format']
        command = f'curl -X PUT --data "artist={artist}&album={album}&track={track}&up_title={up_title}&' \
                  f'up_duration={up_duration_min}:{up_duration_sec}&up_format={up_format}" http://127.0.0.1:5000/'
        os.system(command)
        return redirect(url_for('test_get'))


@app.route('/delete', methods=['POST', 'GET'])
def test_delete():
    if request.method == 'GET':
        return render_template('delete.html')
    elif request.method == 'POST':
        artist = request.form['artist']
        album = request.form['album']
        track = request.form['track']
        command = f'curl -X DELETE --data "artist={artist}&album={album}&track={track}" http://127.0.0.1:5000/'
        os.system(command)
        return redirect(url_for('test_get'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Music(Resource):
    music_dict = {
        'linkin park': [{'album': 'meteora', 'tracklist': [{'title': 'numb', 'duration': '3:05', 'format': 'mp3'},
                                                           {'title': 'faint', 'duration': '2:42', 'format': 'mp3'}],
                         'metadata': {'year': '2003'}},
                        {'album': 'hybrid theory',
                         'tracklist': [{'title': 'in the end', 'duration': '3:36', 'format': 'mp3'},
                                       {'title': 'forgotten', 'duration': '3:14', 'format': 'mp3'}],
                         'metadata': {'year': '2000'}}],
        'korn': [{'album': 'fallow the leader', 'tracklist': [{'title': 'got the life', 'duration': '3:45',
                                                               'format': 'mp3'}], 'metadata': {'year': '1998'}}],
        'limp bizkit': [{'album': 'results may vary', 'tracklist': [{'title': 'eat you alive', 'duration': '4:12',
                                                                     'format': 'mp3'}], 'metadata': {'year': '2003'}}],
        'pla': [{'album': 'pla', 'tracklist': [{'title': 'pla', 'duration': '4:12',
                                                'format': 'mp3'}], 'metadata': {'year': '2003'}}],

    }

    def get(self):
        return self.music_dict

    def post(self):
        artist = request.form['artist'].lower()
        album = request.form['album'].lower()
        track = request.form['track'].lower()
        duration = request.form['duration'].lower()
        song_format = request.form['format'].lower()
        year = request.form['year'].lower()
        if artist in self.music_dict:
            for artist_album in self.music_dict[artist]:
                if album in artist_album['album']:
                    for album_track in artist_album['tracklist']:
                        if track in album_track['title']:
                            return "Song already exist in db :)"
                        else:
                            artist_album['tracklist'].append({'title': track, 'duration': duration,
                                                              'format': song_format})
                else:
                    self.music_dict[artist].append({'album': album, 'tracklist': [{'title': track, 'duration': duration,
                                                                                   'format': song_format}],
                                                    'metadata': {'year': year}})
        else:
            self.music_dict[artist] = [{'album': album, 'tracklist': [{'title': track, 'duration': duration,
                                                                       'format': song_format}],
                                        'metadata': {'year': year}}]
        return 'Song has been added'

    def put(self):
        artist = request.form['artist'].lower()
        album = request.form['album'].lower()
        track = request.form['track'].lower()
        up_title = request.form['up_title'].lower()
        up_duration = request.form['up_duration'].lower()
        up_format = request.form['up_format'].lower()
        if artist in self.music_dict:
            for artist_album in self.music_dict[artist]:
                if album in artist_album['album']:
                    for album_track in artist_album['tracklist']:
                        if track in album_track['title']:
                            album_track['title'] = up_title
                            album_track['duration'] = up_duration
                            album_track['format'] = up_format
                            return 'Song has been updated'
                        else:
                            return 'Invalid data'

    def delete(self):

        artist = request.form['artist'].lower()
        album = request.form['album'].lower()
        track = request.form['track'].lower()
        if artist in self.music_dict:
            for artist_album in self.music_dict[artist]:
                if album in artist_album['album']:
                    for album_track in artist_album['tracklist']:
                        if track in album_track['title']:
                            song_id = artist_album['tracklist'].index(album_track)
                            artist_album['tracklist'].pop(song_id)
                    if len(artist_album['tracklist']) == 0:
                        album_id = self.music_dict[artist].index(artist_album)
                        self.music_dict[artist].pop(album_id)
                        if len(self.music_dict[artist]) == 0:
                            self.music_dict.pop(artist)


api.add_resource(Music, '/')

if __name__ == '__main__':
    app.run(debug=True)

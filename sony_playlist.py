#coding:utf-8

import os

DETERMINE_EXT = ['mp3', 'm4a', 'wma', 'flac']
DETERMINE_EXT = DETERMINE_EXT + map(str.upper, DETERMINE_EXT)


class SonyPlayList(object):
    def __init__(self, _location, _save_dir):
        self.location = _location
        self.save_dir = _save_dir

    def _window_slant(self, p):
        return p.replace('/', '\\')

    def _music_path(self, device_path, filename):
        return '/{}'.format(os.path.join(device_path, filename))

    def _save_m3u8(self, filename, contents):
        save_path = os.path.join(self.save_dir, filename)
        if os.path.exists(save_path):
            print 'exists [{}]'.format(save_path)
            return
        with open(save_path, 'w') as fs:
            fs.writelines(contents)

    def build_playlist(self, _top_dir, _dir=None):
        if not _dir: _dir = self.location
        for (dirpath, dirnames, filenames) in os.walk(_dir):
            contents = []
            relative_path = dirpath[dirpath.rindex(_top_dir):]
            for _file in filenames:
                if _file.split('.')[-1] in DETERMINE_EXT:
                    filename = '{}.{}'.format(relative_path.replace('/', '_'), 'm3u8')
                    music_path = self._window_slant(self._music_path(relative_path, _file))
                    contents.append('{}\n'.format(music_path))
            if contents: self._save_m3u8(filename, contents)
                

if __name__ == '__main__':
    #/Volumes/WALKMAN/MUSIC
    _dir = '/Volumes/WALKMAN/MUSIC'
    #_dir = '/Users/saml/workspace/labs/p'
    sp = SonyPlayList(_dir, '/Users/saml/Desktop/Playlists2')
    sp.build_playlist(os.path.split(_dir)[-1])


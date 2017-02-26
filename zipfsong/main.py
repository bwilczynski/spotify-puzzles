import sys

header = sys.stdin.readline().split()
lines, pickcount = int(header[0]), int(header[1])
songs = []

for i in xrange(1, lines + 1):
    line = sys.stdin.readline()
    songdata = line.split()
    count, name = int(songdata[0]), songdata[1]
    songs.append(((i + 1) * count, name))

res = map(
    lambda song: song[1],
    sorted(songs, key=lambda song: song[0], reverse=True)[:pickcount])

for songname in res:
    print(songname)

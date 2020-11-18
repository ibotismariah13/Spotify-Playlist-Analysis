"""
Copyright Mariah Bolden 2020

this program analyzes spotify playlist from txt files.
the spotify play list are in a eddited date and time format from that used by
JOEL LEHMAN avilable at http://joellehman.com/playlist/index.html
the goal is to analyzie if certain events in peoples lives can be predicted based on how many and what songs they add to playlist
I am starting out with my personal spotify, then explanding with hopefully my apple playlist.

"""
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt


def read_data(sf):
    with open(sf) as file:
        playlist = []
        for line in file:
            song = line.split('        ')
            date = song[1]
            time = song[3]
            time = time.split(':')
            title = song[4]
            artist = song[5]
            album = song[6]
            album = album.rstrip('\n')
            song = [date, time, title, artist]
            playlist.append(song)
    return playlist


def get_most_common_day(pl):
    """
    creates a dicionary and finds the most common date and returns it
    """

    counts = {}
    for song in pl:
        if song[0][0] not in counts:
            counts[song[0]] = 1  # adds a word to the dictonary
        else:
            counts[song[0]] += 1  # counts the dictonary
    data = sorted(counts, key=counts.get, reverse=True)
    return [data[0], counts[data[0]]]


def get_most_common_hour(pl):
    """creates a dicionary and finds the most common hour and returns it"""
    counts = {}
    for song in pl:
        if song[1][0] not in counts:
            counts[song[1][0]] = 1  # adds a word to the dictonary
        else:
            counts[song[1][0]] += 1  # counts the dictonary
    data = sorted(counts, key=counts.get, reverse=True)
    return [data[0], counts[data[0]]]


def get_top_artist(pl):
    """creates a dicionary and finds the most common artist and returns it"""

    counts = {}
    for song in pl:
        if song[3] not in counts:
            counts[song[3]] = 1  # adds a word to the dictonary
        else:
            counts[song[3]] += 1  # counts the dictonary
    data = sorted(counts, key=counts.get, reverse=True)
    return [data[0], counts[data[0]]]


def playlist_info(pl, name):
    """returns a string about the general information about a playlist"""
    num = len(pl)
    day = get_most_common_day(pl)
    hour = get_most_common_hour(pl)
    if int(hour[0]) > 12:
        h = str(int(hour[0]) - 12) + 'PM-' + str(int(hour[0]) - 11) + 'PM'
    elif int(hour[0]) == 0:
        h = '12AM-1AM'
    elif int(hour[0]) == 12:
        h = '12PM-1PM'
    else:
        h = str(hour[0]) + 'AM-' + str(int(hour[0])+1) + 'AM'
    artist = get_top_artist(pl)
    sd = pl[0][0]
    ed = pl[num - 1][0]
    print('\n', name, ' contains ', num, ' songs added between ', sd, ' and ', ed,
          '.\n', round((day[1] / num * 100), 2), '% of songs were added on', day[0], 'the day most songs were added',
          '.\n', round((hour[1] / num * 100), 2), '% of songs were added between ', h,
          '.\nThe most common artist is ',
          artist[0], ' with ', round((artist[1] / num * 100), 2), '% of the songs in the playlist.')


def chart(lists):
    for pl in lists:
        x = []
        y = []

        for song in pl:
            x.append(mdates.datestr2num(str(song[0]),default=None))
            y.append(int(song[1][0]))

        #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        #plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval))
        #plt.scatter(x, y)
        plt.plot_date(x, y)
        plt.gcf().autofmt_xdate()
    plt.show()


def main():
    pl1 = read_data('GaCo_Road_Trip.txt')
    pl2 = read_data('mood.txt')
    pl3 = read_data('why.txt')
    pl4 = read_data('ari.txt')
    pl5 = read_data('robot_reveals.txt')
    pl6 = read_data('transfer.txt')
    pl7 = read_data('cel.txt')
    pl8 = read_data('STSLBD.txt')
    pl9 = read_data('working.txt')
    pl10 = read_data('emo.txt')
    pl11 = read_data('classic.txt')
    pl12 = read_data('shower.txt')
    pl13 = read_data('BYH.txt')
    playlists = pl1 + pl2 + pl3 + pl4 + pl5 + pl6 + pl7 + pl8 + pl9 + pl10 + pl11 + pl12 + pl13
    # get info about each playlist
    playlist_info(pl1, 'Road Trip')
    playlist_info(pl2,'A Fucking Mood')
    playlist_info(pl3, 'Why')
    playlist_info(pl4, 'Ari')
    playlist_info(pl5, 'Robot Reveals')
    playlist_info(pl6, 'transformation')
    playlist_info(pl7, 'Celtic Eagle Luminassenger')
    playlist_info(pl8, 'Songs that shouldnt slap but do')
    playlist_info(pl9, 'Working it')
    playlist_info(pl10, 'Emo Emus')
    playlist_info(pl11, 'Classic Vibes')
    playlist_info(pl12, 'Shower')
    playlist_info(pl3, 'Bless your heart')
    playlist_info(playlists, 'All Playlists')
    #pls = [pl1, pl2, pl3, pl4, pl5, pl6, pl7, pl8, pl9, pl10, pl11, pl12, pl13]
    #chart(pls)


    ''' for song in pl1:
            x.append(str(song[0]))
            y.append((song[1][0]))
    
        plt.scatter(x, y)
        plt.show()'''

if __name__ == '__main__':
    main()

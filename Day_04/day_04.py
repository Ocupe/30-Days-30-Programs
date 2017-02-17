#
# This program is a simple offline database for youtube channels and their videos
# it adds videos to the database and can check for new videos
#

from bs4 import BeautifulSoup
import requests
from pony.orm import *
import logging as log

log.basicConfig(format='[%(levelname)s] %(message)s', level=log.DEBUG)

db = Database()
sql_debug(False)


class Video(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel = Required('Channel')
    title = Required(str)
    watched = Required(bool, default=False)
    url = Required(str)


class Channel(db.Entity):
    name = PrimaryKey(str)
    url = Required(str)
    unseen = Optional(int, default=0)
    videos = Set(Video)


db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)


@db_session
def update_channel(channel_objs):
    for channel in channel_objs:
        html = requests.get('https://www.youtube.com/user/{}/videos'.format(channel.name))
        soup = BeautifulSoup(html.text, 'html.parser')
        grid = soup.select('#channels-browse-content-grid > li')
        for li in grid:
            _item = li.select('h3 > a')[0]
            title = _item['title']
            href = _item['href']
            # if video is not in db add it to the db
            if title not in channel.videos.title:
                log.debug('add video: {}'.format(title))
                Video(channel=channel, title=title, watched=False, url=href)
                commit()
            else:
                log.debug('title already in db: {}'.format(title))


@db_session
def add_channel(channel_name):
    try:
        channel_url = 'https://www.youtube.com/user/{}'.format(channel_name)
        r = requests.get(channel_url)
        if r.status_code == 200:
            log.info('Valid Channel')
        else:
            log.info('Error while checking channel name')
        Channel(name=channel_name, url=channel_url)
        commit()
    except:
        pass


@db_session
def get_channels():
    test_channel = Channel.select()
    return test_channel


channel_list = ['Blender Foundation', 'LastWeekTonight', 'Computerphile', 'Numberphile', 'Tom Scott',
                'Two Minute Papers', 'Vsauce']

if __name__ == '__main__':
    # for item in channel_list:
    #     add_channel(item.replace(' ', ''))
    channels = get_channels()
    update_channel(channels)

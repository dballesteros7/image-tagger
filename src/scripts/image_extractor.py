import calendar
import datetime

import flickrapi

from secrets import api_key

flickr = flickrapi.FlickrAPI(api_key)

minimum_date = datetime.date(2013, 1, 1)
zurich_bbox = '8.4473194545,47.345815342,8.6254413,47.4346662'

interesting_photos = flickr.photos_search(
    min_taken_date=calendar.timegm(minimum_date.timetuple()),
    bbox=zurich_bbox, accuracy=11, safe_search=1, content_type=1,
    has_geo=1, per_page=250)

for photo in interesting_photos.find('photos').findall('photo'):
    url = 'https://farm{farm}.staticflickr.com/{server}/'\
          '{id}_{secret}.jpg'.format(**photo.attrib)

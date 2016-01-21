#!/usr/bin/env python

from requests import get
from sanetime import time, delta
from bs4 import BeautifulSoup as bs
from icalendar import Calendar, Event, vText

cal = Calendar()
cal.add('prodid', '-//NBA on ESPN//espn.go.com/nba/schedule//')
cal.add('version', '2.0')
def display_cal(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

r = get("http://espn.go.com/nba/schedule")
nba_tv_sched = bs(r.text, 'html.parser')
watch_espn = nba_tv_sched.select('img[alt=WatchESPN]')
for game in watch_espn:
    row = game.parent.parent.parent
    cells = row.select('td')
    away = cells[0].select('a > abbr')[0]['title']
    home = cells[1].select('a > abbr')[0]['title']
    start = cells[2]['data-date'] # in GMT
    start_time = time(start)
    duration = delta(minutes=30,hours=2)
    end_time = start_time + duration
    url = cells[3].select('a')[1]['href']

    event = Event()
    event.add('summary', away + ' at ' + home)
    event.add('dtstart', start_time.datetime)
    event.add('dtend', end_time.datetime)
    event.add('dtstamp', time().datetime)
    event['location'] = vText('WatchESPN')
    event['url'] = url
    cal.add_component(event)

print(display_cal(cal))

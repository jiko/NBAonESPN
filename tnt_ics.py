#!/usr/bin/env python

import requests
import json
from sanetime import time, delta
from icalendar import Calendar, Event, vText

cal = Calendar()
cal.add('prodid', '-//NBA on TNT//http://www.nba.com/nbaontnt///')
cal.add('version', '2.0')

def display_cal(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

network = "TNT"
url = "http://data.nba.com/jsonp/5s/json/cms/2014/tntot/games.json?callback=NBAONTNTschedule"
r = requests.get(url)
text = r.text.rstrip("();").replace("NBAONTNTschedule(","")
nba_tv_sched = json.loads(text)
games = nba_tv_sched['sports_content']['games']

for game in games:
    begins = game['gameDateTime'].replace(" ET","")
    duration = delta(minutes=30,hours=2)
    start_time = time(begins, tz='America/New_York')
    end_time = start_time + duration

    event = Event()
    event.add('summary', game['visitor'] + " @ " + game['home'])
    event.add('dtstart', start_time.datetime)
    event.add('dtend', end_time.datetime)
    event.add('dtstamp', time().datetime)
    event['location'] = vText(network)
    if game['tntOt']:
        event['url'] = "http://www.nba.com/tntovertime/"
    cal.add_component(event)

#print(display_cal(cal))
with open('nba_on_tnt.ics', 'wb') as f:
    f.write(cal.to_ical().replace('\r\n', '\n'))

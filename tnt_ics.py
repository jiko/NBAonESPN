#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta
import pytz
import os

# throw out everything before February
months = {"Apr": 4, "May": 5}
cal = Calendar()
cal.add('prodid', '-//NBA on TNT//http://www.nba.com/nbaontnt///')
cal.add('version', '2.0')
timezone = pytz.timezone("US/Eastern")

def display_cal(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

def make_event(game, month, day):
    game_details = game.text.split()
    time = game_details[0]
    hour_minute = time.split(":")
    hour = int(hour_minute[0]) + 12
    minute = int(hour_minute[1][:2])

    duration = timedelta(minutes=25,hours=2)

    start_time = datetime(2015,month,day,hour,minute,0)
    end_time = start_time + duration

    event = Event()
    event.add('summary', " ".join(game_details[1:]))
    event.add('dtstart', timezone.localize(start_time))
    event.add('dtend', timezone.localize(end_time))
    event.add('dtstamp', timezone.localize(datetime.now()))
    event['location'] = vText(network)
    if game.img:
        event['url'] = url
    return event

# download of http://www.nba.com/nbaontnt/
url = "http://www.nba.com/tntovertime/"
network = "TNT"
nba_tv_sched = bs(open("nbaontnt-playoffs.html"))
schedule_table = nba_tv_sched("tbody")
schedule = bs(str(schedule_table))
table_rows = schedule('tr')
games = [bs(str(game)) for game in table_rows]
for game in games:
    g = game('td')
    date = g[0].text.split(", ")[1]
    month_day = date.split()
    if month_day[0] in months.keys():
        month = months[month_day[0]]
        day = int(month_day[1])
        for i in range(1,4):
            if g[i].text:
                cal.add_component(make_event(g[i], month, day))


#print(display_cal(cal))
with open('nba_on_tnt.ics', 'wb') as f:
    f.write(cal.to_ical())

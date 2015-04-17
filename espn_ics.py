#!/usr/bin/env python

from bs4 import BeautifulSoup as bs
from icalendar import Calendar, Event, vText
from datetime import datetime, timedelta
import pytz
import os

cal = Calendar()
cal.add('prodid', '-//NBA on ESPN//espn.go.com/nba/television//')
cal.add('version', '2.0')
timezone = pytz.timezone("US/Eastern")
def display_cal(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

# download of http://espn.go.com/nba/television
nba_tv_sched = bs(open("espn.go.com-nba-playoffs.html"))
schedule_table = nba_tv_sched.select("tbody")
schedule = bs(str(schedule_table))
table_rows = schedule.find_all('tr')
games = [bs(str(game)) for game in table_rows]
for game in games:
    g = game.select('td')
    if len(g) == 4:
        month = 4
        day = int(g[0].text.split()[1])

        time_pm_tz = g[2].text.split()
        split_t = time_pm_tz[0].split(":")
        hour = int(split_t[0])
        # assuming all games begin after noon
        if hour < 12: hour += 12
        minute = int(split_t[1])

        duration = timedelta(minutes=25,hours=2)

        start_time = datetime(2015,month,day,hour,minute,0)
        end_time = start_time + duration

        network = g[3].img['alt']

        event = Event()
        event.add('summary', g[1].text)
        event.add('dtstart', timezone.localize(start_time))
        event.add('dtend', timezone.localize(end_time))
        event.add('dtstamp', timezone.localize(datetime.now()))
        event['location'] = vText(network)
        if "ESPN" in network:
            event['url'] = g[3].a['href']
        cal.add_component(event)

#print(display_cal(cal))
with open('nba_on_espn.ics', 'wb') as f:
    f.write(cal.to_ical())

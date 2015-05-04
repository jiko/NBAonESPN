#!/usr/bin/env python

from requests import get
from sanetime import time, delta
from bs4 import BeautifulSoup as bs
from icalendar import Calendar, Event, vText

cal = Calendar()
cal.add('prodid', '-//NBA on ESPN//espn.go.com/nba/television//')
cal.add('version', '2.0')
def display_cal(cal):
    return cal.to_ical().replace('\r\n', '\n').strip()

r = get("http://espn.go.com/nba/television")
nba_tv_sched = bs(r.text)
schedule_table = nba_tv_sched.select("table.tablehead")
schedule = bs(str(schedule_table))
table_rows = schedule.find_all('tr')
for game in table_rows:
    if game['class'][0] != "colhead" and game['class'][0] != "stathead":
        g = game.select('td')
        start_time = time(" ".join(["May", g[0].text, g[2].text]), tz='America/New_York')
        duration = delta(minutes=30,hours=2)
        end_time = start_time + duration

        event = Event()
        event.add('summary', g[1].text)
        event.add('dtstart', start_time.datetime)
        event.add('dtend', end_time.datetime)
        event.add('dtstamp', time().datetime)
        network = g[3].img['alt']
        event['location'] = vText(network)
        if "ESPN" in network:
            event['url'] = g[3].a['href']
        cal.add_component(event)

print(display_cal(cal))

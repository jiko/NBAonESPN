#!/usr/bin/env python

from bs4 import BeautifulSoup as bs


nba_tv_sched = bs(open("nbaontnt.html"))
schedule_table = nba_tv_sched(id="nbaTNTsched")
schedule = bs(str(schedule_table))
table_rows = schedule('tr')
games = [bs(str(game)) for game in table_rows]
for game in games:
    g = game('td')
    date = g[0].text
    print(date)
    game1_details = g[1].text.split()
    time1 = game1_details[0]
    hour_minute = time1.split(":")
    hour = hour_minute[0]
    minute = hour_minute[1][:2]
    print(" ".join(game1_details[1:]) + " " + hour + " " + minute)
    if g[2].text:
        game2_details = g[2].text.split()
        time2 = game2_details[0]
        hour_minute = time2.split(":")
        hour = hour_minute[0]
        minute = hour_minute[1][:2]
        print(" ".join(game2_details[1:]) + " " + hour + " " + minute)


#!/usr/bin/env python

from bs4 import BeautifulSoup as bs


nba_tv_sched = bs(open("espn.go.com-nba-television.html"))
schedule_table = nba_tv_sched.select("div#my-teams-table table")
schedule = bs(str(schedule_table))
table_rows = schedule.find_all('tr')
games = [bs(str(game)) for game in table_rows]
for game in games:
    g = game.select('td')
    if len(g) == 4:
        if g[0].text in ["JANUARY","FEBRUARY","MARCH","APRIL"]:
            month = g[0].text.capitalize()
            continue
        else:
            print(g[0].text.split()[1] + " "+ month + " " + g[2].text
                    + "\t" + g[1].text)

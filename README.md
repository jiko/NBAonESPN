# NBA on ESPN iCalendar file generator

I wanted an iCalendar file to keep track of what NBA games ESPN shows, like what I found for the [KU Men's Basketball schedule](http://www.kuathletics.com/schedule.aspx?path=mbball&print=true&version=1).

So, this script takes [the NBA on ESPN schedule](http://espn.go.com/nba/television) from the web and turns it into an iCalendar file. It assumes a 2 hour and 15 minute game time, which seems wrong.

This script does not

- Download a copy of the schedule webpage
- Auto-update the file hosted here or on my server
- Note what network the game is on
- Watch the NBA for you
- Link to Watch ESPN online
- Include anything other than team match-ups and times
- Include the full NBA schedule
- Feed your cat

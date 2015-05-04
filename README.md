# NBA on ESPN iCalendar file generator

I wanted an iCalendar file to keep track of what NBA games ESPN shows, like what I found for the [KU Men's Basketball schedule](http://www.kuathletics.com/schedule.aspx?path=mbball&print=true&version=1).

So, this script takes [the NBA on ESPN schedule](http://espn.go.com/nba/television) from the web and turns it into an [NBA on ESPN iCalendar file](http://fortheloveofbasketball.com/nba_on_espn.ics). It assumes a 2 hour and 25 minute game time.

I also made a script to make an [NBA on TNT iCalendar file](http://fortheloveofbasketball.com/nba_on_tnt.ics), based on [the NBA on TNT webpage](http://www.nba.com/nbaontnt/).

These scripts run daily on my server, so the iCalendar files should stay up to date for the playoffs. I have noticed that some of the listings for 'if needed' games have strange timestamps, so keep that in mind.

To install dependencies:

`pip install requests beautifulsoup4 sanetime icalendar`

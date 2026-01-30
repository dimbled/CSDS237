#IMPORTS
import datetime

# Display the current date and time in 'US/Pacific' time zone.
_tz = datetime.timezone(datetime.timedelta(hours=-8)) # create the time zone relative to UTC (DST is in effect)
_dt = datetime.datetime.now(_tz) # get the time

print(_dt) # display the time

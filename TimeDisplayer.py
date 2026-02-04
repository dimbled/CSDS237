#IMPORTS
import datetime

# Display the current date and time in 'US/Pacific' time zone.
_tz = datetime.timezone(datetime.timedelta(hours=-8)) # create the time zone relative to UTC (DST is in effect)
_dt = datetime.datetime.now(_tz) # get the time

print(f"The current date and time in the US/Pacific time zone is {_dt}."
      f"\nFor reference, the current date and time here in Cleveland is {datetime.datetime.now()}") # display the time
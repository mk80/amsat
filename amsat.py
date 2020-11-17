from skyfield.api import Topos, load, EarthSatellite
from datetime import datetime
from pytz import timezone

#stations_url = 'http://celestrak.com/NORAD/elements/amateur.txt'
stations_url = 'https://www.amsat.org/tle/current/nasabare.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

ts = load.timescale()

# San Diego
home = Topos('32.48 N', '117.22 W')

print(datetime.today())
today = datetime.today()
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)

# timeframe to search for passes
plus_time = 2
t0 = ts.utc(today.year, today.month, today.day, today.hour)
t1 = ts.utc(today.year, today.month, today.day + plus_time)


# testing with just ISS
by_name = {sat.name: sat for sat in satellites}
#satellite = by_name['ISS']
satellite = by_name['AO-07']
print(satellite)

t, events = satellite.find_events(home, t0, t1, altitude_degrees=10.0)
for ti, event in zip(t, events):
        name = ('rise above 10°', 'culminate', 'set below 10°')[event]
        print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)


'''
# loop for all satellites... there are a lot...
for sat in satellites:
    print(sat)
    t, events = sat.find_events(home, t0, t1, altitude_degrees=30.0)
    for ti, event in zip(t, events):
        name = ('rise above 30°', 'culminate', 'set below 30°')[event]
        print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
'''

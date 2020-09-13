from skyfield.api import Topos, load, EarthSatellite
from datetime import datetime
from pytz import timezone

#stations_url = 'http://celestrak.com/NORAD/elements/amateur.txt'
stations_url = 'https://www.amsat.org/tle/current/nasabare.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

ts = load.timescale()

home = Topos('32.4809 N', '117.2250 W')

print(datetime.today())
today = datetime.today()
print(today.year)
print(today.month)
print(today.day)

t0 = ts.utc(today.year, today.month, today.day)
t1 = ts.utc(today.year, today.month, today.day + 1)

for sat in satellites:
    print(sat)
    t, events = sat.find_events(home, t0, t1, altitude_degrees=30.0)
    for ti, event in zip(t, events):
        name = ('rise above 30°', 'culminate', 'set below 30°')[event]
        print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
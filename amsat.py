from skyfield.api import Topos, load, EarthSatellite

stations_url = 'http://celestrak.com/NORAD/elements/amateur.txt'
satellites = load.tle_file(stations_url)
print('Loaded', len(satellites), 'satellites')

ts = load.timescale()

home = Topos('32.4809 N', '117.2250 W')
t0 = ts.utc(2020, 9, 13)
t1 = ts.utc(2020, 9, 14)

for sat in satellites:
    print(sat)
    t, events = sat.find_events(home, t0, t1, altitude_degrees=1.0)
    for ti, event in zip(t, events):
        name = ('rise above 1°', 'culminate', 'set below 1°')[event]
        print(ti.utc_strftime('%Y %b %d %H:%M:%S'), name)
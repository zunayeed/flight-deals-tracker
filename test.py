from pprint import pprint
all_flights =  [{'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png',
                  'carbon_emissions': {'difference_percent': 27,
                                       'this_flight': 1371000,
                                       'typical_for_this_route': 1079000},
                  'departure_token': 'WyJDalJJVUUxUVV6VmpkMVJpUjI5QlIyYzFUV2RDUnkwdExTMHRMWFozYUdreU1pMXVNa0ZCUVVGQlIzQjFSbUZqU0hCQ2NYbEJFZ3RGU3pJeU1ueEZTelU0TkJvTENLZktDQkFDR2dOVlUwUTRISENueWdnPSIsW1siREZXIiwiMjAyNi0wOC0wNiIsIkRYQiIsbnVsbCwiRUsiLCIyMjIiXSxbIkRYQiIsIjIwMjYtMDgtMDciLCJEQUMiLG51bGwsIkVLIiwiNTg0Il1dXQ==',
                  'flights': [{'airline': 'Emirates',
                               'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png',
                               'airplane': 'Boeing 777',
                               'arrival_airport': {'id': 'DXB',
                                                   'name': 'Dubai '
                                                           'International '
                                                           'Airport',
                                                   'time': '2026-08-07 13:00'},
                               'departure_airport': {'id': 'DFW',
                                                     'name': 'Dallas Fort '
                                                             'Worth '
                                                             'International '
                                                             'Airport',
                                                     'time': '2026-08-06 '
                                                             '12:15'},
                               'duration': 945,
                               'extensions': ['Above average legroom (32 in)',
                                              'Wi-Fi for a fee',
                                              'In-seat power & USB outlets',
                                              'On-demand video',
                                              'Carbon emissions estimate: '
                                              '1100 kg'],
                               'flight_number': 'EK 222',
                               'legroom': '32 in',
                               'overnight': True,
                               'travel_class': 'Economy'},
                              {'airline': 'Emirates',
                               'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/EK.png',
                               'airplane': 'Boeing 777',
                               'arrival_airport': {'id': 'DAC',
                                                   'name': 'Hazrat Shahjalal '
                                                           'International '
                                                           'Airport',
                                                   'time': '2026-08-07 23:20'},
                               'departure_airport': {'id': 'DXB',
                                                     'name': 'Dubai '
                                                             'International '
                                                             'Airport',
                                                     'time': '2026-08-07 '
                                                             '16:45'},
                               'duration': 275,
                               'extensions': ['Above average legroom (32 in)',
                                              'Wi-Fi for a fee',
                                              'In-seat power & USB outlets',
                                              'On-demand video',
                                              'Carbon emissions estimate: 271 '
                                              'kg'],
                               'flight_number': 'EK 584',
                               'legroom': '32 in',
                               'travel_class': 'Economy'}],
                  'layovers': [{'duration': 225,
                                'id': 'DXB',
                                'name': 'Dubai International Airport'}],
                  'price': 1406,
                  'total_duration': 1445,
                  'type': 'Round trip'},
                 {'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/QR.png',
                  'carbon_emissions': {'difference_percent': 0,
                                       'this_flight': 1080000,
                                       'typical_for_this_route': 1079000},
                  'departure_token': 'WyJDalJJVUUxUVV6VmpkMVJpUjI5QlIyYzFUV2RDUnkwdExTMHRMWFozYUdreU1pMXVNa0ZCUVVGQlIzQjFSbUZqU0hCQ2NYbEJFZ3RSVWpjek1IeFJVall6T0JvTENQdk1DQkFDR2dOVlUwUTRISEQ3ekFnPSIsW1siREZXIiwiMjAyNi0wOC0wNiIsIkRPSCIsbnVsbCwiUVIiLCI3MzAiXSxbIkRPSCIsIjIwMjYtMDgtMDciLCJEQUMiLG51bGwsIlFSIiwiNjM4Il1dXQ==',
                  'flights': [{'airline': 'Qatar Airways',
                               'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/QR.png',
                               'airplane': 'Airbus A350',
                               'arrival_airport': {'id': 'DOH',
                                                   'name': 'Hamad '
                                                           'International '
                                                           'Airport',
                                                   'time': '2026-08-07 17:30'},
                               'departure_airport': {'id': 'DFW',
                                                     'name': 'Dallas Fort '
                                                             'Worth '
                                                             'International '
                                                             'Airport',
                                                     'time': '2026-08-06 '
                                                             '18:20'},
                               'duration': 910,
                               'extensions': ['Average legroom (31 in)',
                                              'Free Wi-Fi',
                                              'In-seat power & USB outlets',
                                              'On-demand video',
                                              'Carbon emissions estimate: 765 '
                                              'kg'],
                               'flight_number': 'QR 730',
                               'legroom': '31 in',
                               'often_delayed_by_over_30_min': True,
                               'overnight': True,
                               'ticket_also_sold_by': ['American', 'Alaska'],
                               'travel_class': 'Economy'},
                              {'airline': 'Qatar Airways',
                               'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/QR.png',
                               'airplane': 'Boeing 777',
                               'arrival_airport': {'id': 'DAC',
                                                   'name': 'Hazrat Shahjalal '
                                                           'International '
                                                           'Airport',
                                                   'time': '2026-08-08 02:40'},
                               'departure_airport': {'id': 'DOH',
                                                     'name': 'Hamad '
                                                             'International '
                                                             'Airport',
                                                     'time': '2026-08-07 '
                                                             '18:25'},
                               'duration': 315,
                               'extensions': ['Average legroom (31 in)',
                                              'Free Wi-Fi',
                                              'In-seat power & USB outlets',
                                              'On-demand video',
                                              'Carbon emissions estimate: 314 '
                                              'kg'],
                               'flight_number': 'QR 638',
                               'legroom': '31 in',
                               'overnight': True,
                               'ticket_also_sold_by': ['American', 'Alaska'],
                               'travel_class': 'Economy'}],
                  'layovers': [{'duration': 55,
                                'id': 'DOH',
                                'name': 'Hamad International Airport'}],
                  'price': 1410,
                  'total_duration': 1280,
                  'type': 'Round trip'},
                 {'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TK.png',
                  'carbon_emissions': {'difference_percent': -11,
                                       'this_flight': 964000,
                                       'typical_for_this_route': 1079000},
                  'departure_token': 'WyJDalJJVUUxUVV6VmpkMVJpUjI5QlIyYzFUV2RDUnkwdExTMHRMWFozYUdreU1pMXVNa0ZCUVVGQlIzQjFSbUZqU0hCQ2NYbEJFZ3RVU3pFNU1ueFVTemN4TWhvTENPUFBDQkFDR2dOVlUwUTRISERqendnPSIsW1siREZXIiwiMjAyNi0wOC0wNiIsIklTVCIsbnVsbCwiVEsiLCIxOTIiXSxbIklTVCIsIjIwMjYtMDgtMDciLCJEQUMiLG51bGwsIlRLIiwiNzEyIl1dXQ==',
                  'flights': [{'airline': 'Turkish Airlines',
                               'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TK.png',
                               'airplane': 'Airbus A350',
                               'arrival_airport': {'id': 'IST',
                                                   'name': 'Istanbul Airport',
                                                   'time': '2026-08-07 17:25'},
                               'departure_airport': {'id': 'DFW',
                                                     'name': 'Dallas Fort '
                                                             'Worth '
                                                             'International '
                                                             'Airport',
                                                     'time': '2026-08-06 '
                                                             '21:30'},
                               'duration': 715,
                               'extensions': ['Average legroom (31 in)',
                                              'Wi-Fi for a fee',
                                              'In-seat USB outlet',
                                              'On-demand video',
                                              'Carbon emissions estimate: 584 '
                                              'kg'],
                               'flight_number': 'TK 192',
                               'legroom': '31 in',
                               'often_delayed_by_over_30_min': True,
                               'overnight': True,
                               'travel_class': 'Economy'},
                              {'airline': 'Turkish Airlines',
                               'airline_logo': 'https://www.gstatic.com/flights/airline_logos/70px/TK.png',
                               'airplane': 'Airbus A330',
                               'arrival_airport': {'id': 'DAC',
                                                   'name': 'Hazrat Shahjalal '
                                                           'International '
                                                           'Airport',
                                                   'time': '2026-08-08 05:15'},
                               'departure_airport': {'id': 'IST',
                                                     'name': 'Istanbul '
                                                             'Airport',
                                                     'time': '2026-08-07 '
                                                             '18:40'},
                               'duration': 455,
                               'extensions': ['Average legroom (31 in)',
                                              'Wi-Fi for a fee',
                                              'In-seat power & USB outlets',
                                              'On-demand video',
                                              'Carbon emissions estimate: 379 '
                                              'kg'],
                               'flight_number': 'TK 712',
                               'legroom': '31 in',
                               'overnight': True,
                               'travel_class': 'Economy'}],
                  'layovers': [{'duration': 75,
                                'id': 'IST',
                                'name': 'Istanbul Airport'}],
                  'price': 1413,
                  'total_duration': 1245,
                  'type': 'Round trip'}],

first_flight = all_flights[0]
pprint((first_flight[1]))
# Now first_flight is a dictionary, so this key lookup works!
#lowest_price = first_flight["price"]

#print(lowest_price)  # Outputs: 1406


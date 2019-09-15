from datetime import date, datetime

Y = 2000
seasons = [('W', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('Sp', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('Su', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('F', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('W', (date(Y, 12, 21),  date(Y, 12, 31)))]

def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)


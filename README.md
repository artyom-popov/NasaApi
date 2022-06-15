# Пример работы

input:

`enter start date yyyy-mm-dd: 2015-01-01` 

`enter end date yyyy-mm-dd (feed date limit 7 days): 2015-01-08` максимально допустимый NASA Api период - 7 дней

`enter limit: 2` количество наибольших космических объектов за день

output:

`{'2015-01-05': {'2523915': {'name': '523915 (1997 VM4)', 'absolute_magnitude_h': 18.2, 'is_potentially_hazardous_asteroid': False}, '3625729': {'name': '(2013 BM76)', 'absolute_magnitude_h': 20.2, 'is_potentially_hazardous_asteroid': False}}, '2015-01-06': {'2434007': {'name': '434007 (2000 VH61)', 'absolute_magnitude_h': 18.4, 'is_potentially_hazardous_asteroid': False}, '54231658': {'name': '(2021 YJ)', 'absolute_magnitude_h': 19.9, 'is_potentially_hazardous_asteroid': True}}, '2015-01-03': {'3711166': {'name': '(2015 DY53)', 'absolute_magnitude_h': 21.4, 'is_potentially_hazardous_asteroid': False}, '3702676': {'name': '(2014 XD32)', 'absolute_magnitude_h': 21.6, 'is_potentially_hazardous_asteroid': False}}, '2015-01-04': {'3781027': {'name': '(2017 QS17)', 'absolute_magnitude_h': 19.85, 'is_potentially_hazardous_asteroid': False}, '2429736': {'name': '429736 (2011 MB2)', 'absolute_magnitude_h': 20.3, 'is_potentially_hazardous_asteroid': False}}, '2015-01-01': {'54244776': {'name': '(2022 BJ8)', 'absolute_magnitude_h': 19.64, 'is_potentially_hazardous_asteroid': False}, '3696406': {'name': '(2014 WL6)', 'absolute_magnitude_h': 20.0, 'is_potentially_hazardous_asteroid': False}}, '2015-01-02': {'2496327': {'name': '496327 (2013 MY6)', 'absolute_magnitude_h': 17.95, 'is_potentially_hazardous_asteroid': False}, '2190208': {'name': '190208 (2006 AQ)', 'absolute_magnitude_h': 18.2, 'is_potentially_hazardous_asteroid': False}}, '2015-01-07': {'54201812': {'name': '(2021 TL)', 'absolute_magnitude_h': 23.39, 'is_potentially_hazardous_asteroid': False}, '3704153': {'name': '(2015 BE4)', 'absolute_magnitude_h': 23.7, 'is_potentially_hazardous_asteroid': False}}, '2015-01-08': {'2343098': {'name': '343098 (2009 DV42)', 'absolute_magnitude_h': 18.62, 'is_potentially_hazardous_asteroid': False}, '3595776': {'name': '(2012 AC11)', 'absolute_magnitude_h': 22.2, 'is_potentially_hazardous_asteroid': False}}}`

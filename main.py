import requests

_KEY = 'HFNVhLXEOOIrepoZjurU6A7kxTUtN51OciMJZz7j'


def get_objs(start_date: str, end_date: str) -> dict:
    timeout = 30
    rq = requests.get(f'https://api.nasa.gov/neo/rest/v1/feed',
                      params={'start_date': start_date, 'end_date': end_date, 'api_key': _KEY}, timeout=timeout)
    assert rq.ok
    return rq.json()['near_earth_objects']


def search_objs(start_date: str, end_date: str, limit: int = 1) -> dict:  # res function
    keys = ['name', 'absolute_magnitude_h', 'is_potentially_hazardous_asteroid']
    res = {}
    objs = get_objs(start_date, end_date)
    for date in objs:
        d_objs = objs[date]
        d_objs.sort(key=lambda obj: obj['absolute_magnitude_h'])
        res[date] = {}
        for obj in d_objs[:limit]:
            res[date][obj['neo_reference_id']] = {key: obj[key] for key in keys}
    return res


def main():
    start_date = input('enter start date yyyy-mm-dd: ')
    end_date = input('enter end date yyyy-mm-dd (feed date limit 7 days): ')
    limit = int(input('enter limit: '))
    print(search_objs(start_date, end_date, limit))


if __name__ == '__main__':
    main()

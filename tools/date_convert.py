"""Convert an explicitly zoned ISO timestamp to UTC."""
import argparse,datetime

def to_utc(text):
    """Reject ambiguous local timestamps instead of assuming the machine time zone."""
    value=datetime.datetime.fromisoformat(text.replace('Z','+00:00'))
    if value.tzinfo is None:raise ValueError('Include a UTC offset in the timestamp')
    return value.astimezone(datetime.timezone.utc).isoformat().replace('+00:00','Z')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('timestamp');a=p.parse_args();print(to_utc(a.timestamp))

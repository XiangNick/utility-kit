"""Small numeric statistics helper."""
import argparse,json,math,statistics

def summary(values):
    """Require finite values and distinguish an empty input from a zero mean."""
    data=[float(x) for x in values]
    if not data:return {'count':0}
    if not all(math.isfinite(x) for x in data):raise ValueError('Finite numbers required')
    return {'count':len(data),'min':min(data),'max':max(data),'mean':statistics.fmean(data),'median':statistics.median(data)}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('values',nargs='*');a=p.parse_args();print(json.dumps(summary(a.values)))

"""Canonical JSON formatting to standard output."""
import argparse,json,pathlib

def format_json(text):
    """Sort object keys while preserving array order and Unicode text."""
    return json.dumps(json.loads(text),ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False)+'\n'

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('file');a=p.parse_args();print(format_json(pathlib.Path(a.file).read_text()),end='')

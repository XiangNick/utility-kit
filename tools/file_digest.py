"""Streaming file digest utility."""
import argparse,hashlib,pathlib

def digest(path,algorithm='sha256'):
    """Read in bounded chunks so large files do not fill memory."""
    value=hashlib.new(algorithm)
    with pathlib.Path(path).open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):value.update(block)
    return value.hexdigest()

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('files',nargs='+');args=parser.parse_args()
    for path in args.files:print(digest(path),path)

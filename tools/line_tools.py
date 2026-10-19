"""Plain text line normalization."""
import argparse,pathlib

def unique_lines(text,case_sensitive=True):
    """Preserve first occurrence order while ignoring empty surrounding space."""
    seen=set();result=[]
    for line in text.splitlines():
        item=line.strip();key=item if case_sensitive else item.casefold()
        if item and key not in seen:seen.add(key);result.append(item)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('file');parser.add_argument('--ignore-case',action='store_true');a=parser.parse_args()
    print('\n'.join(unique_lines(pathlib.Path(a.file).read_text(),not a.ignore_case)))

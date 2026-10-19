"""List regular files and sizes within an explicitly selected directory."""
import argparse,json,os,pathlib

def inventory(directory):
    """Do not follow symbolic links outside the requested tree."""
    root=pathlib.Path(directory);rows=[]
    for base,dirs,files in os.walk(root,followlinks=False):
        dirs[:]=sorted(d for d in dirs if not d.startswith('.') and not (pathlib.Path(base)/d).is_symlink())
        for name in sorted(files):
            path=pathlib.Path(base)/name
            if path.is_file() and not path.is_symlink():rows.append({'path':str(path.relative_to(root)),'bytes':path.stat().st_size})
    return rows

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('directory');a=p.parse_args();print(json.dumps(inventory(a.directory),ensure_ascii=False,indent=2))

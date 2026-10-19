"""Summarize numeric columns without changing the input CSV."""
import argparse,csv,json,math,pathlib

def summarize(path):
    """Ignore missing/non-numeric cells and report the actual numeric sample count."""
    totals={}
    with pathlib.Path(path).open(newline='',encoding='utf-8-sig') as stream:
        for row in csv.DictReader(stream):
            for key,value in row.items():
                try:number=float(value)
                except (ValueError,TypeError):continue
                if not math.isfinite(number):continue
                entry=totals.setdefault(key,{'count':0,'sum':0.0,'min':number,'max':number})
                entry['count']+=1;entry['sum']+=number;entry['min']=min(entry['min'],number);entry['max']=max(entry['max'],number)
    for entry in totals.values():entry['mean']=entry['sum']/entry['count']
    return totals

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('file');a=p.parse_args();print(json.dumps(summarize(a.file),ensure_ascii=False,indent=2))

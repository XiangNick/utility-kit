"""Report structural differences between two JSON documents."""
import argparse,json,pathlib

def compare(left,right,path='$'):
    """Keep types distinct and preserve the path of additions/removals."""
    if type(left) is not type(right):return [{'path':path,'kind':'type'}]
    if isinstance(left,dict):
        rows=[]
        for key in sorted(left.keys()|right.keys()):
            child=path+'['+json.dumps(key,ensure_ascii=False)+']'
            if key not in left:rows.append({'path':child,'kind':'added'})
            elif key not in right:rows.append({'path':child,'kind':'removed'})
            else:rows.extend(compare(left[key],right[key],child))
        return rows
    if isinstance(left,list):
        rows=[]
        for i in range(max(len(left),len(right))):
            child=path+'['+str(i)+']'
            if i>=len(left):rows.append({'path':child,'kind':'added'})
            elif i>=len(right):rows.append({'path':child,'kind':'removed'})
            else:rows.extend(compare(left[i],right[i],child))
        return rows
    return [] if left==right else [{'path':path,'kind':'changed'}]

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('left');p.add_argument('right');a=p.parse_args()
    print(json.dumps(compare(json.loads(pathlib.Path(a.left).read_text()),json.loads(pathlib.Path(a.right).read_text())),ensure_ascii=False,indent=2))

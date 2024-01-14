from src.HW2.config import *
import re, sys, copy, random

def settings(help):
    regex = "[-][-]([\S]+)[^=]+= ([\S]+)"
    res = re.findall(regex, help)
    return dict(res)

def eg():
    return 0

def coerce(s1):
    if s1 == "nil":
        return None
    elif s1 == 'true':
        return True
    elif s1 == 'false':
        return False
    elif s1.isdigit():
        return int(s1)
    elif '.' in s1 and s1.replace('.','').isdigit():
        return float(s1)
    else:
        return s1

def cli(t):
    args = sys.argv[1:]
    for k, v in t.items():
        for n, x in enumerate(args):
            if x == '-'+k[0] or x == '--'+k:
                if v == 'false':
                    v = 'true'
                elif v == 'true':
                    v = 'false'
                else:
                    v = args[n+1]
        t[k] = coerce(v)
    return t
#!/bin/env python3

from multiprocessing import Process
from json import load
from library import  MongoObj, gen_domain, match_tld, gen_req

# Import configuration
with open("config.json", "r") as f:
    config = load(f)["config"]

with open("tld.json", "r") as f:
    tld = load(f)

# def genrun():


# Run only if the files is directly executed by user
if __name__ == '__main__':
    mon = MongoObj()
    mon.db = "test"
    mon.col = "test"
    dom = match_tld(gen_domain(2), tld)
    for l in gen_req(dom):
        mon.insert = l
        mon.mon_write()
        # print(l)



# link = [ yield l[0]+'.'+e for l in gen_domain(2) for e in tld]

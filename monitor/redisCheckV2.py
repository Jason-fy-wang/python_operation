#!/usr/bin/python
# coding=utf-8

import argparse
import os
import time
import sys

BASE = os.getcwd()


def __paramparse():
    parse = argparse.ArgumentParser(description='redis cluster check')
    parse.add_argument('-c', '--cmd', action='store', dest='cmd', required=False, help='cmd to exec.')
    parse.add_argument('-i', '--host', action='store', dest='host', required=True, help='host to check.')
    parse.add_argument('-p', '--port', action='store', dest='port', required=True, help='redis cluster port')
    parse.add_argument('-u', '--user', action='store', dest='user', required=True,help='user use to login host')
    return parse.parse_args()


class CheckRedis:
    """
         check redis cluster
    """
    def __init__(self, hosts, cmd, port, user):
        self.hosts = []
        self.cmd = cmd
        self.port = port
        self.user = user
        if "," in hosts:
            self.hosts = hosts.split(",")
        else:
            self.hosts.append(hosts)

    def __checkinstance(self):
        numinstance = 0
        for hh in self.hosts:
            pcmd = "ssh "+self.user+"@"+hh+"  'source /etc/profile; ps -ef | grep -v grep| grep redis-server | wc -l'"
            res = os.popen(pcmd).readlines()
            numinstance += int(res[0])
        print(numinstance, " instance is running.")

    def __checkworking(self):
        key = time.strftime('%Y%M%d%H%m%S', time.localtime())
        hh = self.hosts[0]
        cc = "set "+key+"  "+key+" EX 50000"
        gg = "get "+key
        scmd = "ssh "+self.user+"@"+hh+"  'source /etc/profile; "+self.cmd+" --cluster call "+hh+":"+self.port+" "+cc+"'"
        gcmd = "ssh "+self.user+"@"+hh+"  'source /etc/profile; "+self.cmd+" --cluster call "+hh+":"+self.port+" "+gg+"'"
        print("key:", key)
        os.popen(scmd)
        res = os.popen(gcmd).readlines()
        for rr in res:
            if key in rr:
                return
        print("redis cluster error.")
        sys.exit(1)


    def check(self):
        self.__checkinstance()
        self.__checkworking()
        print("cluster is working.")

def __getcmdpath():
    cmdpath = os.popen("find /opt -name 'redis-cli'")
    rr = cmdpath.readlines()
    if len(rr) == 0:
        print("cann't find cmd redis-cli")
        sys.exit(1)
    elif len(rr) > 1:
        print("find cmd more than one.")
        sys.exit(1)
    else:
        print("cmd", rr[0])
        return rr[0].replace("\n", "")

def main():
    paser = __paramparse()
    if paser.cmd is not None and "redis-cli" in paser.cmd:
        parms = dict(cmd=paser.cmd, host=paser.host, port=paser.port, user=paser.user)
    else:
        cpath = __getcmdpath()
        parms = dict(cmd=cpath, host=paser.host, port=paser.port, user=paser.user)

    print(parms)
    ck = CheckRedis(parms['host'], parms['cmd'], parms['port'], parms['user'])
    ck.check()

# python checkRedis.py -u root -i 10.163.249.146,10.163.249.147,10.163.249.148 -p 6379  -c /opt/software/redis-cluster/6379/redis-cli

if __name__ == '__main__':
    main()
"""
All the main atributes classes are defined here
"""
import requests, socket
import pymongo
import itertools, string
from pyquery import PyQuery

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 0
    except socket.error:
        return 1

def gen_domain(lenght):
    """
    Generate domain
    """
    letters = string.ascii_lowercase
    first_group = itertools.product(letters, repeat=lenght)
    for elem in itertools.product(first_group):
        yield [''.join(k) for k in elem]

def match_tld(func, tld):
    for l in func:
        yield l[0]+'.'+tld

class MongoObj:
    """
    Connect and read/write to mongo
    """

    def __init__(self, host="mongodb://127.0.0.1:27017", user=None,
                 password=None, out=None, db="pyindex",
                 col="test_mongo", insert=None):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.col = col
        self.out = out
        self.insert = insert

    def mon_con(self):
        """
        Establsih connection to mongodb
        """
        try:
            return pymongo.MongoClient(self.host, username=self.user,
                                       password=self.password)
        except:
            self.out = "Could not connect to {}".format(self.host)

    def mon_list(self):
        """
        List all collections
        """
        try:
            self.out = str(self.mon_con()[self.db].collection_names())
        except:
            self.out = "Could not list collections"

    def mon_write(self):
        try:
            self.mon_con()[self.db][self.col].insert_one(self.insert)
        except:
            self.out = "Could not write to mongodb"

    def __str__(self):
        return self.out


def gen_req(url):
    for l in url:
        if hostname_resolves(l) == 0:
            try:
                result = requests.get("https://"+l, timeout=3)
            except:
                continue
        else:
            continue

        if result.status_code == 200:
            try:
                query = PyQuery(result.text)
                text = query.text()
            except:
                pass
        else:
            text = "HTTP code: {}".format(result.status_code)
        try:
            yield { 'status': result.status_code, 'url': l, 'data': text}
        except:
            yield { 'status': result.status_code, 'url': l, 'data': text}
        else:
            continue

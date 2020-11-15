import json
from seleniumrequests import Chrome
from selenium.webdriver.chrome.options import Options
import unittest2

url = "http://eland.nz:9000/users/"

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
session = Chrome('/opt/bin/chromedriver', chrome_options=chrome_options)

def pp(t, r):
    print("Task '%s' completed - %s" % (t, r))
    j = {}
    try:
        if r.content:
            j = json.loads(r.content)
            print(json.dumps(j, indent=4, sort_keys=True))
    except Exception as e:
        print(e)
        if r.content: print(r.content)
    return j

def listall():
    r = session.request('GET', url)
    pp("List All", r)

def get(id):
    r = session.request('GET', url+id)
    pp("Read", r)

def delete(id):
    try:
        r = session.request('DELETE', url+id)
        pp("Delete", r)
        return "ID: %s deleted - done" % id
    except Exception as e:
        return "ID: %s cannot be deleted - %s" % (id, e)

def postchk(d, j):
    for k in d.keys():
        try:
            if d[k] != j[k]: return k, False
        except Exception as e:
            return e, False
    return '', True

def post(d):
    r = session.request('POST', url, data=d)
    j = pp("Create", r)
    k, b = postchk(d, j)
    if b: 
        return "ID: %s customer created - done" % j["_id"]
    else: 
        delete(j["_id"])
        return "Data error: %s - revoked data" % k

def put(id, d):
    try:
        r = session.request('PUT', url+id, data=d)
        pp("Update", r)
        return "ID: %s updated - done" % id
    except:
        return "ID: %s cannot be updated" % id

class ChromeSearch(unittest2.TestCase):
    def setUp(self):
        print("Start unit tests")

#    def test_delete(self):
#        print("test delete function")
#        ret = delete('5fb088e3c3abc3288dbf35fe')
#        print(ret)
#        self.assertRegex(ret, 'done')

    def test_delete(self):
        print("test delete function")
        ret = post({"name":"Su Kayle","email":"su.keyle@email.com","password":"sukaylepassword","mobile":"042312123","gender":"Female"})
        # ret = post({"name":"Su Kayle","email":"su.keyle@email.com","password":"sukaylepassword"})
        print(ret)
        self.assertRegex(ret, 'done')

if __name__ == '__main__':
    unittest2.main()
    # delete('5fb088e3c3abc3288dbf35fe')
    # put('5fb08833c3abc3288dbf35fc', {"name":"Dam Smith","password":"damsmithpassword"})
    # put('5fb088e3c3abc3288dbf35fe', {"name":"Parv Sing","password":"parsingpassword"})
    # put('5fafe4c7bfd3790e81800940', {"name":"Python Cool","password":"pythoncoolpassword"})
    # post({"name":"Su Kayle","email":"su.keyle@email.com","password":"sukaylepassword","mobile":"042312123","gender":"Female"})
    # listall()
    session.close()

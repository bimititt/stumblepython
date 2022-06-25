import requests, threading, datetime, sys, os, time

def main():
	global auth, maxerr, api, pos, dely
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f"\t  Crown And Trophy Duper")
	print(f"\t\t\tBy: @Lixi Kece")
	print("="*64)
	maxerr = 0 # Avoid Ban when User AFK.
	api = "kitkabackend.eastus.cloudapp.azure.com:5010"
	auth = str(input("Authorization Key: "))
	pos = int(input("""
0 = Round 1 
1 = Round 2 
2 = Round 3 
3 = Round 3 Winner
Input Correctly Or The Script Wont Start
Input: """))
	dely = float(input("\nDelay : "))
	thr = int(input("\nThreads: "))
	print("="*64)
	for _ in range(thr):
	        threading.Thread(target=s).start()

def s():
        global maxerr
        while True:
                dt = datetime.datetime.now()
                try:
                        headers = {
                            'authorization': auth,
                            'use_response_compression': 'true',
                            'Accept-Encoding': 'gzip',
                            'Host': api,
                            'Connection': None,
                            'User-Agent': None,
                        }
                        response = requests.get(f'http://{api}/round/finishv2/{pos}', headers=headers)
                        if response.status_code == 200:
                                trof = response.text.split('"SkillRating":')[1].split(',')[0]
                                cro = response.text.split('"Crowns":')[1].split(',')[0]
                                sys.stdout.write(f"\r[{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}] | Trophy : {trof} | Crowns : {cro}")
                                sys.stdout.flush()
                        elif response.status_code == 403 and response.text == "BANNED":
                                print(f"[{dt.year}-{dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}] Your Account Rest In Peace !")
                                break
                                sys.exit(0)
                        else:
                                maxerr += 1
                                print(f"[{response.status_code}] Failed. Maybe Auth Key Expired?")
                                if maxerr >= 15: # Avoid Ban Detection
                                        break
                                        sys.exit(0)
                        if dely > 0: time.sleep(dely)
                except Exception as e:
                        pass

if __name__ == "__main__":
	main()

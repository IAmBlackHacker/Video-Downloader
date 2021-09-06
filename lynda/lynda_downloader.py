import sys
try:
	from bs4 import BeautifulSoup
	import requests
	import urllib.request
except:
	print('Install\n   bs4, requests, urllib.request module')
	print('   Command python -m pip install requests')
	print('\n   Before that check that you are using python3.x')
	sys.exit()
try:
	if sys.version_info[0] < 3:
		raise "REQUIRED PYTHON 3.x"
except Exception as ex:
	print('''		--------------------------------------
			REQUIRED PYTHON 3.x
			use: python3 assignment.py
		--------------------------------------
			''')
	sys.exit()

token = "09191e10-b89d-4f10-ab91-2ae0ee50832b,73d8ab491dae11ee0fb16ad77c0e91db,m1b1AayDiNoWwja0KlARi2p7zq1pV0k3xCDLOQisvq3nFOBnupgQlz38fxQa4GFm33UHcm/OVwrdfQuiby5OP2JlfRVLimSAsEclZXky+u/ncuizjAF5P4RVgS+uXwAsqFiuynzRiwIQkoAC1jCypg=="

url = input('Enter Url : ')
# Ex : https://www.lynda.com/IT-Infrastructure-tutorials/Hacking-goals/476620/511428-4.html

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
payload = {
	
}
cookies = {
    "__utma": "203495949.555274255.1523552988.1523553004.1523553004.1",
    "__utmb": "203495949.1.9.1523553004",
    "__utmc": "203495949",
    "__utmz": "203495949.1523553004.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "_ga": "GA1.2.555274255.1523552988",
    "_gid": "GA1.2.1634528897.1523552988",
    "LyndaLoginStatus": "Member-Logged-In",
    "throttle-20fc2dfb0a81016faeebb960e94da216": "1",
    "throttle-54c678a5add39d58a7d7411cae569603": "1",
    "throttle-85975e5888b0a2a3d27c273fd5637879": "1",
    "throttle-bf01e020137cb85eaa7a5e6a2f331834": "1",
    "throttle-cb8048294d8a62ec98a5d38754e4a964": "1",
    "throttle-d3ebbd09ec7ecff8c4948ff79599614d": "1",
    "throttle-fcc41b5952df7ea0746eff3c71b72bc7": "1",
    # "utag_main": "v_id:0162bad5aaa0001500a9daea539004073001606b00978$_sn:1$_ss:0$_pn:7%3Bexp-session$_st:1523555460453$ses_id:1523552987808%3Bexp-session",
    # "bcookie": "4e412255b1274bbd88cca0aa4cc32c3cda4ebc4482384e308ddf5010903917ee",
    # "litrk-srcveh": "srcValue=direct/none&vehValue=direct/none&prevSrc=&prevVeh=",
    # "LyndaAccess": "LyndaAccess=4/12/2018 10:11:20 AM&p=0&data=9,12/30/2018,1,191505",
    "ncp": "1",
    "player":"%7B%22volume%22%3A0.8%2C%22muted%22%3Afalse%7D",
    "player_settings_0_2":"player_type=2&video_format=1&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=0",
    "player_settings_1991744043_2":"player_type=2&video_format=1&cc_status=2&window_extra_height=148&volume_percentage=50&resolution=540",
    "show-member-tour-cta":"true",
    "SSOLogin":"OrgUrl=https%3A%2F%2Fwww.lynda.com%2Fportal%2Fsip%3Forg%3Dottawa.ca&OrgName=Ottawa%20Public%20Library",
    # "tcookie":"e3dc8574-6d37-47e5-b4a1-144f616ee131",
    "token":token,
} 
print('Wait checking video url .......')
try:
	html     = requests.get(url,cookies=cookies,headers=headers)
	html     = BeautifulSoup(html.content,'html.parser')
	video    = html.find('video')
	data_src = video['data-src']
except:
	print("\nInvalid URL Error!\n   Ex. https://www.lynda.com/IT-Infrastructure-tutorials/Hacking-goals/476620/511428-4.html\n   For More contact +91 8419027520 (H4K3R)")
	sys.exit(0)
def download_file(url,file_name):
	with open(file_name, "wb") as f:
		print ("   Downloading %s" % file_name)
		response = requests.get(url, stream=True,headers=headers)
		total_length = response.headers.get('content-length')
		if total_length is None:
			f.write(response.content)
		else:
			dl = 0
			total_length = int(total_length)
			print('   Length : '+str(total_length*0.00390625/(4096.0)) + ' MB')
			for data in response.iter_content(chunk_size=4096):
				dl += len(data)
				f.write(data)
				done = int(50 * dl / total_length)
				sys.stdout.write("\r[%s%s] %s" % ('=' * done, ' ' * (50-done),str(done*2)+'%') )    
				sys.stdout.flush()

if '.mp4' in data_src:
	file_name=data_src.split('?')[0].split('/')[-1]
	print('   File Name : '+str(file_name))
	# urllib.request.urlretrieve(data_src, file_name)
	download_file(data_src,file_name)
else:
	print('\n   Check Login Please')
	print('\n   Or(|)   Enter Premium Login Token (Line 6)')
	print('\n   Help(?) You Get Token from cookies after Premium Login')
	print('\n   Contact +91 8419027520 (H4K3R)')

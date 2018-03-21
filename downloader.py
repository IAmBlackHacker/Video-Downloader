import requests
import sys
import os
try:
	if sys.version_info[0] < 3:
		raise "REQUIRED PYTHON 3.x"
except Exception as ex:
	print('''		--------------------------------------
			REQUIRED PYTHON 3.x
			use: python3 download.py
		--------------------------------------
			''')
	sys.exit()

doc="""
      PROGRAM BY h4k3r
        Make sure that you have installed livestreamer and vlc
        Linux   [apt-get install livestreamer vlc]
        Windows [download setup of livestreamer and vlc then install] 
"""
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0',
}
post_url="http://en.fetchfile.net/fetch/"
download_url=input('Enter url : ')
r=requests.post(url=post_url,headers=headers,data={'url':download_url})
if r.status_code==200:
	jsonData=r.json()
	manifest_url=jsonData.get('manifest_url',None)
	if not manifest_url:
		manifest_url=jsonData.get('webpage_url',None)
	if not manifest_url: #jsonData.get('formats',None):
		print('Check internet connection or try again ...')
		sys.exit(0)
	print('----------------------------------------------------')
	print('  Title     : ',jsonData.get('title',None))
	print('  Episode   : ',jsonData.get('episode',None))
	print('  Episode No: ',jsonData.get('episode_number',None))
	print('  Extractor : ',jsonData.get('extractor',None))
	os.system('livestreamer '+manifest_url+' | grep streams')
	# urls=[]
	# for n,i in enumerate(jsonData.get('formats',[])):
	# 	print('           '+str(n)+' : '+str(i.get('width',''))+' x '+str(i.get('height','')))
	# 	print(i.get('url'))
	# 	urls.append(i.get('url'))
	print('----------------------------------------------------')
	choice=input('Enter stream Ex .: ')
	try:
		play=bool(int(input('Play(0) or Download(1) : ')))
	except:
		play=False
	if not play:
		os.system('livestreamer '+manifest_url+' '+choice)
	else:
		os.system('livestreamer '+manifest_url+' '+choice+' -o "'+jsonData.get('title','default')+'.mp4"')
else:
	print('Contact 8419027520 for errors !')


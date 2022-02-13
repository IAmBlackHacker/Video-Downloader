import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser_url = ""
print("------ Video Stream Downloader ------")
print("Supported sites:")
print("1. Hotstar - Supports to download all videos. just you need to get premium account in order to download premium videos")
browser_url = input("\nEnter video url: ")
print("Once the browser will start playing video then your download will start")
print("-------------------------------------")

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get(browser_url)


def is_video_exist(args):
	network_logs = browser.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
	for network_log in network_logs:
		name = network_log.get("name", "")
		if name[-5:] == "1.m4s" and "video_" in name:
			return name
	return False

def is_audio_exist(args):
	network_logs = browser.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
	for network_log in network_logs:
		name = network_log.get("name", "")
		if name[-5:] == "1.m4s" and "audio_" in name:
			return name
	return False

video_url_link = WebDriverWait(browser, 300).until(is_video_exist)
audio_url_link = WebDriverWait(browser, 300).until(is_audio_exist)
video_file_name = "video.mp4"
audio_file_name = "audio.mp4"

browser.get(video_url_link)

headers = {
	'origin': 'https://www.hotstar.com',
	'referer': 'https://www.hotstar.com/'
}
cookies = {}
for cookie in browser.get_cookies():
	cookies[cookie.get("name")] = cookie.get("value")
headers['cookie'] = "; ".join([str(x)+"="+str(y) for x,y in cookies.items()])

browser.close()

def get_content_from_url(content_url):
	content = b''
	r = requests.request("GET", content_url, headers=headers, data={}, stream=True)
	for chunk in r.iter_content(chunk_size=8192):
		content += chunk
	return r.status_code, content

def download_file(file_name, content_url):
	file = open(file_name, 'wb')
	status_code = None
	index = 0
	while status_code != 404:
		if index == 0:
			status_code, content = get_content_from_url(content_url.replace("seg-1.m4s", "init.mp4", 1))
		else:
			status_code, content = get_content_from_url(content_url.replace("1.m4s", str(index) + ".m4s", 1))
		print(status_code, " Writing segment:", index)
		if status_code == 200:
			index += 1
			file.write(content)
	file.close()

print("\nGetting started download video")
download_file(video_file_name, video_url_link)
download_file(audio_file_name, audio_url_link)

print("Download complete ...", video_file_name, audio_file_name)



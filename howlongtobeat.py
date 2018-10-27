import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import googlesearch3
from googlesearch import search


DEBUG=True

def debugPrint(mess):
	if DEBUG:
		print(mess)

def findTimes(title):
	s_query = ' '.join([title, 'howlongtobeat'])
	debugPrint("Looking for playing time :")
	debugPrint(s_query)
	lst = search(s_query, stop = 1)
	top_1 = list(lst)[0]
	req = Request(top_1, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
	webpage = urlopen(req).read()
	html = str(webpage)
	soup = BeautifulSoup(html, 'html.parser')

	game_times_tag = soup.find('div', class_='game_times')
	game_time_list = []
	for li_tag in game_times_tag.find_all('li'):
		title = li_tag.find('h5').text.strip()
		play_time = li_tag.find('div').text.strip()
		game_time_list.append(play_time)
	return int(game_time_list[0].split(' ')[0])



def howlongtobeat(fileName='Games.tsv', test=False):
	with open(fileName, 'r') as file:
		lines = file.readlines()
		lines = lines[1:]

		if test:
			print(findTimes(lines[0].split('\t')[0]))
			return
		
		for line in lines:	
			title = line.split('\t')[0]
			print(findCritic(title))



if __name__=='__main__':
	howlongtobeat(test=True)

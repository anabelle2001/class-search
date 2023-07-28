#!/usr/bin/python3

import requests
import json 
from bs4 import BeautifulSoup
import time
import pickle

root_url = "ssb.cofc.edu"

def make_3_magic_requests(datecode,subj=False):
	first_url = f'https://{root_url}/StudentRegistrationSsb/ssb/term/termSelection?mode=search'

	second_url = f"https://{root_url}/StudentRegistrationSsb/ssb/searchResults/searchResults?{'txt_subject={subj}&' if subj else ''}txt_term={datecode}&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=100&sortColumn=subjectDescription&sortDirection=asc"

	header = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie':'',
		'Connection':'keep-alive',
		'Host':root_url,
		'Referer':(
			f'{root_url}/StudentRegistrationSsb/ssb/classSearch/classSearch' 
		),
		'User-Agent':(
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
			'(KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		),
		'X-Synchronizer-Token':'',
		'X-Requested-With':'XMLHttpRequest',
	}

	header2 = {
		** header,
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept':'*/*',
	}

	my_session = requests.Session()

	first = my_session.get(first_url)
	soup = BeautifulSoup(first.text,'html.parser')
	token = soup.find('meta',{'name':'synchronizerToken'}).attrs['content']

	header['X-Synchronizer-Token'] = token
	header['Cookie'] = 'JSESSIONID'+'='+my_session.cookies['JSESSIONID']

	header2['X-Synchronizer-Token'] = token
	header2['Cookie'] = 'JSESSIONID'+'='+my_session.cookies['JSESSIONID']

	my_session.post(f'https://{root_url}/StudentRegistrationSsb/ssb/term/search?mode=search',data='term={}&studyPath=&studyPathText=&startDatepicker=&endDatepicker='.format(datecode),headers=header2)

	final = my_session.get(second_url,headers=header)
	return json.loads(final.text)

if __name__ == "__main__":
	date = '202310'
	print(make_3_magic_requests(date))
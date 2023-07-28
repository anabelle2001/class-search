#!/usr/bin/python3

import requests
import json 
from bs4 import BeautifulSoup
import time
import pickle

root_url = "ssb.cofc.edu"

def createSession(baseURL,datecode):
	handshakeURL = f'https://{baseURL}/StudentRegistrationSsb/ssb/term/termSelection?mode=search'
	auth_session = requests.Session()
	auth_response = auth_session.get(handshakeURL)
	auth_response_parser = BeautifulSoup(auth_response.text,'html.parser')
	auth_token = auth_response_parser.find('meta',{'name':'synchronizerToken'}).attrs['content']

	final_headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
		'Cookie':f'JSESSIONID={auth_session.cookies["JSESSIONID"]}',
		'Connection':'keep-alive',
		'Host':baseURL,
		'Referer':(
			f'https://{baseURL}/StudentRegistrationSsb/ssb/classSearch/classSearch' 
		),
		'User-Agent':(
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
			'(KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
		),
		'X-Synchronizer-Token':auth_token,
		'X-Requested-With':'XMLHttpRequest',
	}
	
	provisional_headers = {
		** final_headers,
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Accept':'*/*',
	}

	auth_session.post(
		f'https://{baseURL}/StudentRegistrationSsb/ssb/term/search?mode=search',
		data=f'term={datecode}&studyPath=&studyPathText=&startDatepicker=&endDatepicker=',
		headers=provisional_headers
	)

	auth_session.headers = final_headers
	return auth_session

def first50classes(auth_session,datecode):
	subj = None

	second_url = f"https://{root_url}/StudentRegistrationSsb/ssb/searchResults/searchResults?{'txt_subject={subj}&' if subj else ''}txt_term={datecode}&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=100&sortColumn=subjectDescription&sortDirection=asc"
	final = auth_session.get(second_url)
	return json.loads(final.text)

if __name__ == "__main__":
	date = '202310'
	print(first50classes(createSession(root_url,date),date))
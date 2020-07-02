# tests/test_wfpy.py

from pylotus import *
from pytest import fixture, raises

@fixture
def fissure_keys():
	'''Creates a pytest fixture holding any given fissure object's keys.'''
	return ['id', 'activation', 'startString',
			'expiry', 'active', 'node', 'missionType',
			'enemy', 'tier', 'tierNum', 'expired',
			'eta']

@fixture
def cetus_keys():
	'''Creates a pytest fixture holding any given Cetus object's keys.'''
	return ['id', 'activation', 'isDay','expiry', 
			'state', 'timeLeft', 'isCetus', 'shortString']

@fixture
def vallis_keys():
	'''Creates a pytest fixture holding any given Vallis object's keys.'''
	return ['id', 'isWarm','expiry','timeLeft']

@fixture
def news_keys():
	'''Creates a pytest fixture hoding any given Vallis object's keys.'''
	return ["date", "imageLink", "eta", "primeAccess",
			"stream", "translations", "link", "update",
			"id", "asString", "message", "priority"]

def test_wfpy_calls():
	'''Tests the actual API wrapper calls.'''
	assert isinstance(wf_api.get_platforms(), list)

	xbox_wfpy_instance = wf_api('xb1')
	response = xbox_wfpy_instance.get_fissure_info()

	assert (isinstance(response, list) or isinstance(response, dict)), "Response should be either a list of JSON-like dicts or a single JSON-like dict"
	with raises(NonPlatformError):
		wf_api('mobile')
	# TODO: How to test StatusCodeError?


def test_fissure_class(fissure_keys):
	'''Tests an API call to get info on the current in-game fissures.'''

	xbox_wfpy_instance = wf_api('xb1')
	response = xbox_wfpy_instance.get_fissure_info()

	assert (isinstance(response, list) or isinstance(response, dict)), "Response should be a list of fissure JSON-like objects"
	assert set(fissure_keys).issubset(response[0].keys()), "All keys should be in the response"
	assert isinstance(Fissure(response[0]), Fissure), "Fissure should be successfully constructed from a fissure dict"
	assert isinstance(Fissure(response[0]).to_string(), str), ".to_string() should return a str"
	with raises(DictTypeError):
		Fissure('some_fun_string')
		Fissure({'meaning_of_life': 42})


def test_cetusinfo_class(cetus_keys):
	'''Tests an API call to get info on Cetus/the Plains of Eidolon.'''

	xbox_wfpy_instance = wf_api('xb1')
	response = xbox_wfpy_instance.get_cetus_info()

	assert (isinstance(response, list) or isinstance(response, dict)), "Response should be a single JSON-like objects"
	assert set(cetus_keys).issubset(response.keys()), "All keys should be in the response"
	assert isinstance(CetusInfo(response), CetusInfo), "CetusInfo should be successfully constructed from a CetusInfo dict"
	assert isinstance(CetusInfo(response).to_string(), str), ".to_string() should return a str"
	with raises(DictTypeError):
		CetusInfo('some_fun_string')
		CetusInfo({'meaning_of_life': 42})


def test_vallisinfo_class(vallis_keys):
	'''Tests an API call to get info on the Orb Vallis.'''

	xbox_wfpy_instance = wf_api('xb1')
	response = xbox_wfpy_instance.get_vallis_info()

	assert (isinstance(response, list) or isinstance(response, dict)), "Response should be a single JSON-like objects"
	assert set(vallis_keys).issubset(response.keys()), "All keys should be in the response"
	assert isinstance(VallisInfo(response), VallisInfo), "VallisInfo should be successfully constructed from a VallisInfo dict"
	assert isinstance(VallisInfo(response).to_string(), str), ".to_string() should return a str"
	with raises(DictTypeError):
		VallisInfo('some_fun_string')
		VallisInfo({'meaning_of_life': 42})


def test_newsinfo_class(news_keys):
	'''Tests an API call to get info on current in-game news.'''

	xbox_wfpy_instance = wf_api('xb1')
	response = xbox_wfpy_instance.get_news_info()

	assert (isinstance(response, list) or isinstance(response, dict)), "Response should be a list of JSON-like objects"
	assert set(news_keys).issubset(response[0].keys()), "All keys should be in the response"
	assert isinstance(NewsInfo(response[0]), NewsInfo), "NewsInfo should be successfully constructed from a NewsInfo dict"
	assert isinstance(NewsInfo(response[0]).to_string(), str), ".to_string() should return a str"
	with raises(DictTypeError):
		NewsInfo('some_fun_string')
		NewsInfo({'meaning_of_life': 42})


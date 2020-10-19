# pylotus/response_classes.py

from .exceptions import *

class Fissure:
	_fissure_keys = ['id', 'activation', 'startString',
					 'expiry', 'active', 'node', 'missionType',
					 'enemy', 'tier', 'tierNum', 'expired',
					 'eta']

	def __init__(self, fissure_dict):
		if not isinstance(fissure_dict, dict):
			raise DictTypeError('Fissure', fissure_dict)
		for key in self._fissure_keys:
			if key not in fissure_dict.keys():
				raise DictTypeError('Fissure', fissure_dict)
		self.id = fissure_dict['id']
		self.activation = fissure_dict['activation']
		self.startString = fissure_dict['startString']
		self.expiry = fissure_dict['expiry']
		self.active = fissure_dict['active']
		self.node = fissure_dict['node']
		self.missionType = fissure_dict['missionType']
		self.enemy = fissure_dict['enemy']
		self.tier = fissure_dict['tier']
		self.tierNum = fissure_dict['tierNum']
		self.expired = fissure_dict['expired']
		self.eta = fissure_dict['eta']

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _fissure_keys


class CetusInfo:
	_cetus_keys = ['id', 'activation', 'isDay','expiry',
				   'state', 'timeLeft', 'isCetus', 'shortString']

	def __init__(self, cetus_dict):
		if not isinstance(cetus_dict, dict):
			raise DictTypeError('CetusInfo', cetus_dict)
		for key in self._cetus_keys:
			if key not in cetus_dict.keys():
				raise DictTypeError('CetusInfo', cetus_dict)
		self.id = cetus_dict['id']
		self.activation = cetus_dict['activation']
		self.shortString = cetus_dict['shortString']
		self.expiry = cetus_dict['expiry']
		self.isDay = cetus_dict['isDay']
		self.state = cetus_dict['state']
		self.timeLeft = cetus_dict['timeLeft']
		self.isCetus = cetus_dict['isCetus']

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _cetus_keys


class VallisInfo:
	_vallis_keys = ['id', 'isWarm','expiry','timeLeft']

	def __init__(self, vallis_dict):
		if not isinstance(vallis_dict, dict):
			raise DictTypeError('VallisInfo', vallis_dict)
		for key in self._vallis_keys:
			if key not in vallis_dict.keys():
				raise DictTypeError('VallisInfo', valliss_dict)
		self.id = vallis_dict['id']
		self.expiry = vallis_dict['expiry']
		self.isWarm = vallis_dict['isWarm']
		self.timeLeft = vallis_dict['timeLeft']

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _vallis_keys


class NewsInfo:
	_news_keys = ["date", "imageLink", "eta", "primeAccess",
				  "stream", "translations", "link", "update",
				  "id", "asString", "message", "priority"]

	def __init__(self, news_dict):
		if not isinstance(news_dict, dict):
			raise DictTypeError('NewsInfo', news_dict)
		for key in self._news_keys:
			if key not in news_dict.keys():
				raise DictTypeError('NewsInfo', news_dict)
		self.date = news_dict["date"]
		self.imageLink = news_dict["imageLink"]
		self.eta = news_dict["eta"]
		self.primeAccess = news_dict["primeAccess"]
		self.stream = news_dict["stream"]
		self.translations = news_dict["translations"]
		self.link = news_dict["link"]
		self.update = news_dict["update"]
		self.id = news_dict["id"]
		self.asString = news_dict["asString"]
		self.message = news_dict["message"]
		self.priority = news_dict["priority"]

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _news_keys

class Invasion:
	_invasion_keys = ["defenderReward", "attackingFaction",
					  "completion", "attackerReward", "count",
					  "completed", "requiredRuns", "vsInfestation",
					  "node", "eta", "defendingFaction", "id",
					  "activation", "rewardTypes", "desc"]

	def __init__(self, invasion_dict):
		if not isinstance(invasion_dict, dict):
			raise DictTypeError('Invasion', invasion_dict)
		for key in self._invasion_keys:
			if key not in invasion_dict.keys():
				raise DictTypeError('Invasion', invasion_dict)
		self.defenderReward = invasion_dict["defenderReward"]
		self.attackingFaction = invasion_dict["attackingFaction"]
		self.completion = invasion_dict["completion"]
		self.attackerReward = invasion_dict["attackerReward"]
		self.count = invasion_dict["count"]
		self.completed = invasion_dict["completed"]
		self.requiredRuns = invasion_dict["requiredRuns"]
		self.vsInfestation = invasion_dict["vsInfestation"]
		self.node = invasion_dict["node"]
		self.eta = invasion_dict["eta"]
		self.defendingFaction = invasion_dict["defendingFaction"]
		self.id = invasion_dict["id"]
		self.activation = invasion_dict["activation"]
		self.rewardTypes = invasion_dict["rewardTypes"]
		self.desc = invasion_dict["desc"]

	def to_string(self):
		self_string = ''
		for k, v in vars(self).items():
			self_string += k + ': ' + str(v) + '\n'
		return self_string

	def get_expected_keys(self):
		return _invasion_keys
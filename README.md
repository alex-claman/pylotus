# PyLotus

PyLotus is a simple Python wrapper for the Warframe API. 

## Description

This is a super simple wrapper for the Warframe API, information about which can be found [here](https://docs.warframestat.us/). Most requests to the API have been implemented; any that haven't been can be retrieved by requesting the worldstate. Also provided are some basic prebuilt classes to hold common responses like individual ```Fissure``` objects, etc. 

## Dependencies

PyLotus only uses the built-in ```requests``` and ```json``` libraries, with ```pytest``` only being used to implement testing. These are all installable and upgradeable via [pip](https://pip.pypa.io/en/stable/).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyLotus.

```bash
pip install pylotus
```

## Usage

All platforms are supported for use with the API wrapper; a list containing the platform shorthand notations accepted by the API are accessible through the static ```wf_api.get_platforms()```.

```python
from pylotus import *

print(wf_api.get_platforms()) # It's always possible to retrieve all supported platforms with which to construct the API, even in a static context.
```

```python
>>> ['pc', 'ps4', 'xb1', 'swi']
```

Create a ```wf_api``` instance that can access the WarFrame API for a specified platform. Retrieve information from the API with the responses stored in lists of easily accessed JSON-formatted dict objects or individual objects.

```python
xbox_api_wrapper = wf_api('xb1') # Create an instance with your preferred platform.

current_fissures = xbox_api_wrapper.get_current_fissures() # Get back a list of JSON response dicts or a single JSON response dict.

do_something_with_the(current_fissures)
```

Use built-in classes, like the ```Fissure``` class, to easily wrap common API responses. Pass the class constructors the retrieved JSON representations of the API returns.

```python
fissure_objects = [Fissure(fissure) for fissure in current_fissures]

print(len(fissure_objects))
for f in fissure_objects:
	print(type(f), f.enemy, f.missionType)
```

```python
>>> 4
>>> Fissure, Grineer, Defense
>>> Fissure, Corpus, Defense
>>> Fissure, Grineer, Interception
>>> Fissure, Grineer, Mobile Defense
```

You can also import only the API interface, skipping the prebuilt classes if you would rather. Do this by importing as follows:

```python
from pylotus import wf_api
```

## License

Licensed under the [MIT](https://choosealicense.com/licenses/mit/) license. 

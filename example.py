import pylotus

print(pylotus.wf_api.get_platforms())

try:
	incorrect_wf_api = pylotus.wf_api('yikes')
	
except pylotus.NonPlatformError as npe:
	print(npe.message)

xbox_wf_api = pylotus.wf_api('pc')

current_fissures = xbox_wf_api.get_fissure_info()

fissure_objs = [pylotus.Fissure(fissure) for fissure in current_fissures]

for fissure in fissure_objs:
	print(fissure.node)
#import urllib.request
with urllib.request.urlopen('https://www.nexus.ford.com/service/rest/repository/browse/fnv2_private_release_repository/com/ford/ecg/ECG_Bundle_Debug/ECG_Bundle_Debug/') as response:
   html = response.read()
   print (html)

############################################################################

# import urllib.request
#
# print('Beginning file download with urllib2...')
#
# url = 'https://publib.boulder.ibm.com/bpcsamp/v6r1/monitoring/clipsAndTacks/download/ClipsAndTacksF1ForModeler.zip'
# urllib.request.urlretrieve(url, 'C:\\Users\\ga264577\\Desktop\\test\\aa.zip')

#########################################################################################
import os
import requests
#
# url = 'http://gmail.com'
# user, password = 'ganeshprasad20', 'gan123*#'
# resp = requests.get(url, auth=(user, password))
# print (resp.text)



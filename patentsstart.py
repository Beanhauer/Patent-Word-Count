# 
# Example file for parsing and processing JSON
#

import urllib.request # instead of urllib2 like in Python 2.7
import json
def getPatent(data):
  print("patent number: ->",data)

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  print("\nin printResults")
  print(theJSON)
  
  # for p in theJSON['patents']:
  #   print(" PATENT ID " ,p['patent_id']) 
  #   print(" PATENT NAME " ,p['patent_title'])
  #   getPatent(p['patent_id'])
  # now we can access the contents of the JSON like any other Python object
  # if "patent_number" in theJSON["patents"]:
  # print (theJSON["patents"])
  print("\nleaving printResults")
  
def main():
  print("\nStart\n")
  # James.  I would like people to enter the inventor's name here instead of the patent number.
  # 1. Ask for the name
  # 2. Save the name they enter
  # 3. Change the part of this URL that goes to patent_number to go to the inventor name.
  #  (there is a list of the fields at patentsview.org somewhere...help or something)
  # 4. make the inventor field equal to whatever they entered.
  urlx = "https://www.patentsview.org/api/patents/query?q={\"_eq\":{\"patent_number\":\"3930277\"}}&f=[\"patent_number\",\"patent_date\"]"

  print("set url ")
  webUrl = urllib.request.urlopen(urlx)
  print("guess that works")
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
    data = webUrl.read()
  # print out our customized results
    print("\nHere's what was found:\n")
    printResults(data)
  else:
    print("\nDid not reach Patentsview website\n")
  print("\nDone\n")
  

if __name__ == "__main__":
  main()

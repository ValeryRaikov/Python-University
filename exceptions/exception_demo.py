import sys

fIn = 'symbolsIn.csv'
fOut = 'symbolsOut.csv'

try:
   with open(fIn, 'r') as f:
      file_content = f.read()
      print ("read file " + fIn)
   if not file_content:
      print ("no data in file " + fIn)
      file_content = "name,phone,address\n"
   with open(fOut, 'w') as dest:
      dest.write(file_content)
      print ("wrote file " + fOut)
except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))
except:
   print ("Unexpected error:", sys.exc_info()[0])
print ("done")
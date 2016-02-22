import os
os.system('pwd')

fr = open("../read_file.conf", "r")

os.system('sudo rm -rf apache.conf')
os.system('sudo echo '' >> apache.conf')

fo = open("apache.conf", "w")
fo.write(fr.read())
fr.close()
fo.close()

print "File Transfer over"

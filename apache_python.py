import os
os.system('pwd')

fr = open("read_file.conf", "r")

os.system('sudo git clone https://github.com/selfup/PHPOne.git /var/www/html/PHPOne')

os.system('sudo rm -rf /etc/httpd/conf/httpd.conf')
os.system('sudo echo '' >> /etc/httpd/conf/httpd.conf')

fo = open("test/apache.conf", "w")
fo.write(fr.read())
fr.close()
fo.close()

print "File Transfer over"

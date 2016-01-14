import os
import time
source=['/home/crazyacking/swaroop/byte','/home/crazyacking/swaroop/bin']
target_dir='/home/crazyacking/swaroop/bak/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr '%s' %s"%(target,' '.join(source))

if os.system(zip_command)==0:
	print "Successful backup to",target
else:
	print "Backup FAILED!"

import os
import time

source=['/home/crazyacking/swaroop/byte/','/home/crazyacking/swaroop/bin/']
target_dir='/home/crazyacking/swaroop/bak/'
folder_name=time.strftime("%Y%m%d")
create_folder_command='mkdir '+target_dir+folder_name
if not os.path.exists(target_dir+folder_name):
	os.system(create_folder_command)
target_dir+=folder_name+'/'
backup_name=target_dir+time.strftime("%H_%M_%S")+'.zip'
zip_command="zip -qr '%s' %s"%(backup_name,' '.join(source))
if os.system(zip_command)==0:
	print("Successful backup to",backup_name)
else:
	print("Backup FAILED!")

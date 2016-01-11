
from Tools.scripts.treesync import raw_input

file_object=open(r'F:\python\笔记整理\第一章 - 快速改造：基础知识.txt','r')
try:
	all_the_text=file_object.read()
finally:
	file_object.close()

print(all_the_text)

for line in all_the_text:
	line_len=len(line)
	if()
#!/usr/bin/python
# -*- coding: UTF-8 -*- 

# Video Timescale Cal
# >>> 50*60+31
# 3031
# >>> 48*60+47
# 2927
# >>> 44*60+26
# 2666

# Prepare
# cut -d "】" -f 1  ./program_item.md | cut -d " " -f 2 > ./timeRaw
# cut -d "】" -f 2  ./program_item.md > ./detailRaw

section_amount=input('How many sections are there? ')
section[section_amount]=[]

for i in section_amount:
	section[i]=input('Please input the section time length[MM:SS]:')
	section[i] = int(section[i].split(':')[0])*60 + int(section[i].split(':')[1])


# Time Transformed
f_time_raw=open(r'./timeRaw','r')
original_list=f_time_raw.read()
mm_ss_list=original_list.split('\n')
ss_list=[]
mm_in_sec_list=[]
sec_sum_list=[]

mm_ss_list.pop()

for i in range(len(mm_ss_list)):
	x=int(mm_ss_list[i].split(':')[0])
	mm_in_sec_list.append(x)

for i in range(len(mm_ss_list)):
	x=int(mm_ss_list[i].split(':')[1])
	ss_list.append(x)

for i in range(len(mm_in_sec_list)):
	mm_in_sec_list[i]*=60
	sec_sum_list.append(mm_in_sec_list[i]+ss_list[i])

o_time_trans=open(r'./timeTransformed','w')

for i in range(len(sec_sum_list)):
	print(sec_sum_list[i],file=o_time_trans)

o_time_trans.close()


# Time Calculate
f_time_trans=open(r'./timeTransformed','r')
original_list=f_time_trans.read()
sec_list=original_list.split('\n')

sec_list.pop()

for i in range(len(sec_list)):
	sec_list[i]=int(sec_list[i])

for i in range(12,23):
	sec_list[i]=int(sec_list[i])+section[0]

for i in range(23,29):
	sec_list[i]=int(sec_list[i])+section[0]+section[1]

o_time_cal=open(r'./timeOnlyMetadata','w')

for i in range(len(sec_list)):
	print(sec_list[i],file=o_time_cal)

o_time_cal.close()


# Time-Only Metadata Fomat
f_time_cal=open(r'./timeOnlyMetadata','r')
original_sec=str(f_time_cal.split('\n'))

for i in range(len(original_sec)):
	if i != len(original_sec)-1:
		num=original_sec[i+1]-1
		original_sec[i]=str(original_sec[i])+' '+str(num)
	else:
		original_sec[i]=str(original_sec[i])


# Detail Raw Merge
f_detail=open(r'detailRaw','r')
detail_list=f_detail.read()
print(detail_list)
detail_raw_list=detail_list.split('\n')
print(detail_raw)

for i in range(len(detail_raw_list)):
	full_list.append(raw_list[i] + ' _ ' + detail_raw_list[i])

metadata_item=[]

for i in range(len(full_list)):
	metadata_item.append('[CHAPTER]\nTIMEBASE=1/1\nSTART=' + full_list[i].split(' ')[0]  + '\nEND=' + full_list[i].split(' ')[1] + '\ntitle=chapter # ' + full_list[i].split(' _ ')[1])

print(metadata_item)

o_metadata=open(r'./outputMetadata','w')

for i in range(len(metadata_item)):
	print(metadata_item[i],file=o_metadata)

o_metadata.close()


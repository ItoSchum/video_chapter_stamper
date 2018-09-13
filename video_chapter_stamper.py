#!/usr/bin/python3
# -*- coding: UTF-8 -*- 


# Prepare
	# Shell Command
	# cut -d "】" -f 1  ./program_item.md | cut -d " " -f 2 > ./timeRaw
	# cut -d "】" -f 2  ./program_item.md > ./detailRaw


# Raw Program Item Refine
raw_filename = input("Please input the raw file's filename: ")
f_raw = open(r"./" + raw_filename,"r")
raw_full = f_raw.read()
raw_full = raw_full.split("\n")

raw_time_format = []

for i in range(len(raw_full)):
	raw_time_format_item = (raw_full[i].split("】")[0])
	raw_time_format_item = raw_time_format_item.split(" ")[1]  
	raw_time_format.append(raw_time_format_item)
	# print(raw_time_format[i])

raw_detail = []

for i in range(len(raw_full)):
	raw_detail_item = (raw_full[i].split("】")[1])
	raw_detail.append(raw_detail_item)
	# print(raw_detail[i])


# Raw Video Length Calculate
metadata_title = input("Please input the metadata's Title info: ")
metadata_artist = input(" Please input the metadata's Artist info:")
video_section_amount = input("How many sections are there? ")
# video_section_amount = 3
video_section_length = []

for i in range(0, int(video_section_amount)):
	input_format = input("Please input the section time length in [MM:SS] format: ")
	input_in_sec = int(input_format.split(":")[0]) * 60 + int(input_format.split(":")[1])
	video_section_length.append(input_in_sec)
	# print("Video Section " + str(i + 1) + ": " + str(video_section_length[i]) + "s")


# Formatted Time Transformed
sec_sum = []

for i in range(len(raw_time_format)):
	mm_item = int(raw_time_format[i].split(":")[0])
	ss_item = int(raw_time_format[i].split(":")[1])
	sec_sum.append(mm_item * 60 + ss_item)
	# print("sec_sum: " + str(sec_sum[i]) + "s")


# Time In-Sec Modify
for i in range(12, 23):
	sec_sum[i] = sec_sum[i] + video_section_length[0]
	# print("sec_sum Modified: " + str(sec_sum[i]) + "s")

for i in range(23, 29):
	sec_sum[i] = sec_sum[i] + video_section_length[0] + video_section_length[1]
	# print("sec_sum Modified: " + str(sec_sum[i]) + "s")


# Formatted Time-Only Metadata
sec_sum_set = []
for i in range(len(sec_sum)):
	if i != len(sec_sum) - 1:
		sec_sum_sub_one = sec_sum[i + 1] - 1
		sec_sum[i] = str(sec_sum[i]) + " " + str(sec_sum_sub_one)
	else:
		sec_sum[i] = str(sec_sum[i]) + " " + str(video_section_length[0] + video_section_length[1] + video_section_length[2])
	# print("sec_sum set: " + str(sec_sum[i]))


# Detail Raw Merge
metadata_raw = []
metadata = []

for i in range(len(raw_detail)):
	metadata_raw.append(sec_sum[i] + " _ " + raw_detail[i])

for i in range(len(metadata_raw)):
	metadata.append("[CHAPTER]\nTIMEBASE=1/1\nSTART=" + metadata_raw[i].split(" ")[0]  + "\nEND=" + metadata_raw[i].split(" ")[1] + "\ntitle=chapter # " + metadata_raw[i].split(" _ ")[1])
	# print(metadata[i])


o_metadata=open(r"./outputMetadata","w")

print(";FFMETADATA\ntitle=" + metadata_title + "\nartist=" + metadata_artist + "\n", file = o_metadata)
for i in range(len(metadata)):
	print(metadata[i], file = o_metadata)

print("Done.\nMetadata File has been created in your current dir.")
o_metadata.close()


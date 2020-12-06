#!python3
import csv

def import_csv():
	csv_filename = input("Please input the csv filename: ")

	csvfile = open(csv_filename, newline='')
	f_csv_reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
	f_csv = []
	for row in f_csv_reader:
		f_csv.append(row)
		print(' ' * 3, row)
	csvfile.close()	
	return f_csv


def mm_ss_to_second(mm_ss_timestamp):
	minute = int(mm_ss_timestamp.split(':')[0])
	second = int(mm_ss_timestamp.split(':')[1])
	return (minute * 60 + second)


def convet_csv_to_metadata(f_csv, video_duration):
	# convert start_time from str to int
	for row in f_csv:
		row['start_time'] = mm_ss_to_second(row['start_time'])

	# generate end_time as int
	for i in range(len(f_csv)):
		if i != len(f_csv) - 1:
			f_csv[i]['end_time'] = f_csv[i + 1]['start_time'] - 1
		else:
			f_csv[i]['end_time'] = video_duration

	metadata = []
	metadata.append("[CHAPTER]\nTIMEBASE=1/1\nSTART=0" 
			+ "\nEND=" + str(f_csv[1]['start_time'] - 1)
			+ "\ntitle=" + "0. Opening")

	for i in range(len(f_csv)):
		metadata.append("[CHAPTER]\nTIMEBASE=1/1\nSTART=" 
			+ str(f_csv[i]['start_time'])
			+ "\nEND=" + str(f_csv[i]['end_time'])
			+ "\ntitle=" + str(i + 1) + ". " + f_csv[i]['title'])
		# print(metadata[i])

	return metadata


def generate_metadata_file(chapter_metadata, title='Unknown', artist='Unknown'):

	o_metadata=open(r"./chapter_metadata.txt","w")
	print(";FFMETADATA\ntitle=" + title + "\nartist=" + artist + "\n", file = o_metadata)
	for i in range(len(chapter_metadata)):
		print(chapter_metadata[i], file = o_metadata)

	print("Done.\nMetadata File has been generated in your current dir.")
	o_metadata.close()


def main():
	f_csv = import_csv()
	video_duration = input("Please input the vido duration in format [MM:SS]: ")
	video_duration = mm_ss_to_second(video_duration)
	chapter_metadata = convet_csv_to_metadata(f_csv, video_duration)

	title = input("Please input the metadata's Title info: ")
	artist = input("Please input the metadata's Artist info: ")
	generate_metadata_file(chapter_metadata, title, artist)

if __name__ == '__main__':
	main()



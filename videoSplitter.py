from moviepy.editor import *
import metaAdder
import argparse, os

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', '--videopath', type=str, help='File path to the video clip', required=True)
	parser.add_argument('-t', '--timecodepath', type=str, help='File path to the timecodes', required=True)
	parser.add_argument('-y', '--year', type=str, help='Year to be added to the metadata', required=True)
	parser.add_argument('-g', '--genre', type=str, help='Genre to be added to the metadata', required=True)
	parser.add_argument('-a', '--album', type=str, help='Album name to be added to the metadata', required=True)
	parser.add_argument('-f', '--force', help='Forces files to be replaced instead of skipping files that already exist', action='store_true')
	args = parser.parse_args()
	with open(args.timecodepath) as f:
		times = f.readlines()
	clip = VideoFileClip(args.videopath)
	path = os.curdir[:len(os.curdir) - 2] + "clipped"
	if(not os.path.isdir(path)):
		os.mkdir(path)
	prevStartTime = 0
	clipCount = 0
	for i in range(0, len(times) - 1):
		filename = times[i].split(' ')
		filename.pop(0)
		filename = (' '.join(filename))
		timecode = times[i + 1].split(' ')[0]
		timestamp = (int(timecode.split(':')[0]) * 3600) + (int(timecode.split(':')[1]) * 60) + int(timecode.split(':')[2])	
		if (os.path.exists(path + '/' + filename[:len(filename)-1] + '.mp3') and not args.force):
			print('"' + filename[:len(filename)-1] + '"\n\talready exists, skipping to next item\n')
			prevStartTime = timestamp
			continue
		sclip = clip.subclip(prevStartTime, timestamp).audio
		sclip.write_audiofile(path + '/' + filename[:len(filename)-1] + '.mp3', nbytes=2)
		prevStartTime = timestamp
		clipCount += 1
		metaAdder.add_meta(path + '/' + filename[:len(filename)-1] + '.mp3', args.album, i + 1, len(times) + 1, args.year, args.genre)

	filename = times[len(times) - 1].split(' ')
	filename.pop(0)
	filename = (' '.join(filename))
	if (os.path.exists(path + '/' + filename[:len(filename)-1] + '.mp3') and not args.force):
		print('"' + filename[:len(filename)-1] + '"\n\talready exists, skipping to next item\n')
	else:
		timestamp = clip.duration
		sclip = clip.subclip(prevStartTime, timestamp).audio
		sclip.write_audiofile(path + '/' + filename[:len(filename)-1] + '.mp3', nbytes=2)
		del sclip
		metaAdder.add_meta(path + '/' + filename[:len(filename)-1] + '.mp3', args.album, len(times) + 1, len(times) + 1, args.year, args.genre)
	del clip
	print("Completed")
if(__name__ == "__main__"):
	main()
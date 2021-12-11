![alt-text](https://raw.githubusercontent.com/tnk-rin/walls/main/VideoSplitter.png "Logo")

# videoSplitter
A small tool to clip music compilations from youtube into individual songs.

## How it works
Can be run with the command
`python videoSplitter.py`
##

Required Arguments:

`-v (--videopath) filename`    Path to the video to split

`-t (--timecodepath) filename` Path to the timecode file

Metadata Arguments (Optional):

`-y (--year) year`

`-g (--genre) genre`

`-a (--album) album`

Other Arguments:

`-f (--force)`                 Converts all songs, even if it is already present in output folder

## The timecode file

An [example timecode file](https://github.com/tnk-rin/videoSplitter/blob/master/example_timecode.txt) has been added to the repository but it follows the simple format:

```
HH:MM:SS Artist Name - Track Name
HH:MM:SS Artist Name - Track Name
...
```

__The time listed is the start time of each song.__

## Dependencies
Needs moviepy and mutagen
`pip install moviepy mutagen`

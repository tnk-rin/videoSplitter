![alt-text](https://raw.githubusercontent.com/tnk-rin/walls/main/VideoSplitter.png "Logo")

# videoSplitter
This is a small tool to clip music compilations from youtube into individual songs.

## How it works
The splitter can be run with the command
`python videoSplitter.py`
##

Required Arguments:

`-v (--videopath) filename`    Path to the video to split

`-t (--timecodepath) filename` Path to the timecode file

Optional Arguments:

`-y (--year) year`             The year to apply to the metadata

`-g (--genre) genre`           The genre to apply to the metadata

`-a (--album) album`           The album name to apply to the metadata

`-f (--force)`                 If the song already exists in the output folder, overwrite it

# The timecode file

An [example timecode file](https://github.com/tnk-rin/videoSplitter/blob/master/example_timecode.txt) has been added to the repository but it follows the simple format:

```
HH:MM:SS Artist Name - Track Name
HH:MM:SS Artist Name - Track Name
...
```

__The time listed is the start time of each song.__

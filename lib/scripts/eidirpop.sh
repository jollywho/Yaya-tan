loc="/home/chishiki/Movies"

#loop on each directory in loc as top
#loop on each subdirectory as second
#if second contains a directory, move that directory to top
#rename second to [](filename)[] of first item in its dir as ndir
#if top contains ndir, move contents of ndir into top/ndir
find $loc -iname '*.*' | while read file; do
  basename "$file" | python fname_strip.py
done

#find $loc -type d -empty -delete

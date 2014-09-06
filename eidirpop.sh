loc="/home/chishiki/Movies/test"

#loop on each directory in loc as top
#loop on each subdirectory as second
#if second contains a directory, move that directory to top
#rename second to [](filename)[] of first item in its dir as ndir
#if top contains ndir, move contents of ndir into top/ndir

for top in $(ls -d $loc/*); do
  for second in $(ls -d $top/*); do
    if [[ -d $second ]]; then
      echo $top
      echo $second
      base=$(basename $second)
      match=$(expr match "$base" '.*_\([a-zA-Z]\+\)_')
      if [ "$match" == "" ]; then
        echo "match"
        #python fname_strip.py
      fi
      #mv $second $loc
    fi
  done
done

find $loc -type d -empty -delete

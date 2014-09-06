strip_audio()
{
  a=$(mktemp).mkv
  ffmpeg -i $1 -map 0:0 -map 0:$2 -acodec copy -vcodec copy $a
  if [ $? -eq 0 ]; then
    rm $1
    mv $a $1
  fi
}


lst=$(pwd)
if [ $# -gt 1 ]; then
  strip_audio $1 $2
else
  for i in $lst/* ; do
  strip_audio $i $1
  done
fi

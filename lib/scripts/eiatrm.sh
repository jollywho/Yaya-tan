strip_audio()
{
  a=$(mktemp).mkv
  ffmpeg -i "$1" -map 0:0 -c:v copy -map 0:2 -c:a copy -map 0:3 -c:s copy "$a"
  if [ $? -eq 0 ]; then
    rm "$1"
    mv "$a" "$1"
  fi
}

lst=$(pwd)
if [ $# -gt 1 ]; then
  strip_audio "$1" "$2"
else
  find "$lst" -type f -name '*.*' -print0 | \
    while IFS= read -r -d '' file; do
      strip_audio "$file" "$1"
      exit
  done
fi

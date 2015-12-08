if [ "$HOSTNAME" == casper ]; then
  YFSDIR=${HOME}
elif [ "$HOSTNAME" == balthasar ]; then
  YFSDIR=${HOME}/casper
fi
YFSDIR="${YFSDIR}/YFS/ALL"

find "${1}" -iname '*.*' | while read file; do

#if good extension
shopt -s nocasematch
if [[ "${file}" =~ ^.*\.(mkv|avi|mp4|ogm)$ ]]; then

  # if eidata supplied
  if [ $# -gt 1 ]; then
    filename=$(basename "$file")
    name="$2"
  else
    filename=$(basename "$file")
    dest=$(echo "$filename" | eidata )
    name=$(echo $dest | cut -d " " -f1)
  fi

  # if a valid name is returned
  if [ -n $name ]; then

    new_YFSDIR="$YFSDIR"/"$name"
    new_file=${new_YFSDIR}/$(basename "${filename}")

    mkdir -p "$new_YFSDIR"

    #if file doesnt exist (to prevent overwrite)
    if [ ! -f "$new_file" ]; then
      mv -i "$file" "$new_YFSDIR"
    fi

  fi
fi
done

#delete empty directories
#find "${1}" -type d -empty -delete

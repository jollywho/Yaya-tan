loc="${HOME}/YFS/ALL"

find "$1" -iname '*.*' | while read file; do

  # if eidata supplied
  if [ $# -gt 1 ]; then
    filename="$1"
    name="$2"
  else
    filename=$(basename "$file")
    dest=$(echo "$filename" | eidata )
    name=$(echo $dest | cut -d " " -f1)
  fi

  # if a valid name is returned
  if [ -n $name ]; then

    new_loc=$loc/$name
    new_file=${new_loc}/$(basename ${filename})

    mkdir -p $new_loc

    #if file doesnt exist (to prevent overwrite)
    if [ ! -f "$new_file" ]; then
      mv -i "$file" "$new_loc"
    fi

  fi
done

#delete empty directories
find $loc -type d -empty -delete

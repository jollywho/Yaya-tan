loc="/mnt/casper/chishiki/ALL"

find $loc -iname '*.*' | while read file; do

  filename=$(basename "$file")
  dest=$(echo "$filename" | python fname_strip.py)
  name=$(echo $dest | cut -d " " -f1)
  ep=$(echo $dest | cut -d " " -f2)

  if [[ -n $dest ]]; then

    new_loc=$loc/$name
    new_file=$new_loc/$filename

    mkdir -p $new_loc

    #if file doesnt exist (to prevent overwrite)
    if [ ! -f "$new_file" ]; then
      mv -i "$file" "$new_loc"
    fi

  fi
done

#delete empty directories
find $loc -type d -empty -delete

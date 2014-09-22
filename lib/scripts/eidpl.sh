pend="/dev/sr0: writable, no read permission"
res=$(sudo file -s /dev/sr0)
printf "waiting..."
while [[ $res == $pend ]]
do
  res=$(sudo file -s /dev/sr0)
done
printf "done.\n"
sudo mount /dev/sr0 /media/1
a=$(find /media/1 -type f -printf x | wc -c)
b=$(find /media/1 -type d -printf x | wc -c)
casper_path=/mnt/casper/chishiki/dvds
if [[ $a -gt 0 || $b -gt 1 ]]; then
  printf "starting..."
  temp=$(mktemp -d $casper_path/XXXXX) && chmod -R +rw $temp
  sudo cp -rf /media/1/* $temp
  sudo chmod -R +rw $temp
  sudo chown -R chishiki $temp
  printf "done.\n"
  tput setaf 2
  banner -C --font=2 '##DONE##'
  tput setaf 5
  printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' -
  sudo umount /media/1
  eject
else
  printf "not run"
fi

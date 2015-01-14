if [ "$HOSTNAME" == casper ]; then
  EIIDIR='/usr/share/eii/lib'
elif [ "$HOSTNAME" = melchior ]; then
  EIIDIR='/mnt/eii/lib'
fi
EIICMD="${EIIDIR}/eii.sh"

gen_data()
{
  #if good extension
  shopt -s nocasematch
  if [[ "${1}" =~ ^.*\.(mkv|avi|mp4|ogm)$ ]]; then
    bname="$(basename "$1")"
    data=($(echo "${bname}" | eidata ))
    set_data ${data[@]}
  fi
}

set_data()
{
  name=$1
  ep=$2
  sub=$3
  check=$4
  echo $name $ep $sub $check
}

load_to_db()
{
  name=$1
  ep=$2
  sub=$3
  check=$4

  #attempt to add name to EII
  $(. ${EIICMD} -i -t master -v ${name} 2> /dev/null)

  #get master_id for name from EII
  args="-s -x -t master -c id -f name -v ${name}"
  m_id=$(. ${EIICMD} ${args})

  #if valid master_id then add file data to EII
  if [ -n ${m_id} ]; then
    args="-i -r -t file -v"
    $(. ${EIICMD} ${args} ${m_id} "${name}" ${ep} ${sub} ${check} 2> /dev/null)
  fi
}

if [ -f "${1}" ]; then
  load_to_db $(set_data "${@:2}")
else
  find "${1}" -iname '*.*' | while read file; do
    load_to_db $(gen_data "${file}")
  done
fi

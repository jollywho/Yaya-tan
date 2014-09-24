EIIDIR='/home/chishiki/qp/eii/lib'
EIICMD="${EIIDIR}/eii.sh"

gen_data()
{
  bname="$(basename "$1")"
  data=($(echo "${bname}" | eidata ))
  set_data ${data[@]}
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
  m_id=$(. ${EIICMD} ${args} | cut -d$'\n' -f 2 2> /dev/null)

  #if valid master_id then add file data to EII
  if [ -n ${m_id} ]; then
    args="-i -r -t file -v"
    $(. ${EIICMD} ${args} ${m_id} "${bname}" ${ep} ${sub} ${check} 2> /dev/null)
  fi
}

if [ $# -gt 1 ]; then
  load_to_db $(set_data $@)
else
  find "$1" -iname '*.*' | while read file; do
    echo "${file}"
    load_to_db $(gen_data "${file}")
  done
fi

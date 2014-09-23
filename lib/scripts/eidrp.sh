EIIDIR='/home/chishiki/qp/eii/lib'
EIICMD="${EIIDIR}/eii.sh"

data=($(basename $1 | eidata ))

name=${data[0]}
ep=${data[1]}
sub=${data[2]}
check=${data[3]}

#attempt to add name to EII
$(. ${EIICMD} -i -t master -v ${name} 2> /dev/null)

#get master_id for name from EII
args="-s -x -t master -c id -f name -v ${name}"
m_id=$(. ${EIICMD} ${args} | cut -d$'\n' -f 2 2> /dev/null)

#if valid master_id then add file data to EII
if [ -n ${m_id} ]; then
  args="-i -r -t file -v"
  $(. ${EIICMD} ${args} ${m_id} ${name} ${sub} ${check} 2> /dev/null)
fi

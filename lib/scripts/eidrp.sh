EIIDIR='/home/chishiki/qp/eii/lib'
EIICMD="${EIIDIR}/eii.sh"

data=($(basename $1 | eidata ))

name=${data[0]}
ep=${data[1]}
group=${data[2]}
check=${data[3]}

m_id=$(. ${EIICMD} -s -x -t master -c id -f name -v "Air" | cut -d$'\n' -f 2)

. ${EIICMD} -i -r -t file -v $m_id $name

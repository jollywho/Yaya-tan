# escape if no arguments given
if [[ -z $@ ]]; then
  exit
fi

red='\\e[0;31m'
yellow='\\e[0;33m'
cyan='\\e[0;36m'
green='\\e[0;32m'
NC='\\e[0m'

str=$@

# translate spaces to '+' in search string
m=${str// /+}
a=$(mktemp)
b=$(mktemp)
c=$(mktemp)
d=$(mktemp)

# scrape search page
url=$(wget -q -O- http://nibl.co.uk/bots.php?search=$m \
  | sed 's/<td class="\(botname\|packnumber\|filesize\|filename\)">/<td class="\1">\n/g')

# set xpath and attributes to extract
bot="/html/body/div/div/div/table/tr/td[@class = 'botname']/text()"
pack="/html/body/div/div/div/table/tr/td[@class = 'packnumber']/text()"
size="/html/body/div/div/div/table/tr/td[@class = 'filesize']/text()"
name="/html/body/div/div/div/table/tr/td[@class = 'filename']/text()"

# extract pack details and surround with escape colors
echo -e "$url" | xmllint --html --xpath "$bot" --format - \
  | sed '/^\s*$/d' | sed 's/^/'"${yellow}"'/' | sed 's/\s*$/'"${NC}"'/' > $a
echo -e "$url" | xmllint --html --xpath "$pack" --format - \
  | sed '/^\s*$/d' | sed 's/^/'"${cyan}"'/' | sed 's/$/'"${NC}"'/' > $b
echo -e "$url" | xmllint --html --xpath "$size" --format - \
  | sed '/^\s*$/d' | sed 's/^/'"${red}"'/' | sed 's/$/'"${NC}"'/' > $c
echo -e "$url" | xmllint --html --xpath "$name" --format - \
  | sed '/^\s*$/d' | sed 's/^/'"${green}"'/' | sed 's/$/'"${NC}"'/' > $d
ret=$(paste -d '\t' $a $b $c $d)
rm $a $b $c $d
o=$(echo -e "$ret" | sed 's/\t/||/g')

trap "exit 0" SIGINT
# show contents with line numbers
echo -e "$o" | less -N
read item

if [ $item = 'q' ]; then
  exit
fi

# e.g. 0 2 5 -> 0p;2p;5p
# e.g. 1-5 -> 1,5p
item=$(echo "$item" | sed -e 's/\([0-9]*\)-\([0-9]*\)/\1,\2p/g' \
  | sed -e 's/\([0-9^,p]*\)/\1p;/g' | sed -e 's/pp/p/g')

msg=$(echo -e "$ret" | sed -n "${item}")
clip=$(echo "$msg" | perl -pe 's/\e\[?.*?[\@-~]//g')

# iterate batch selection and combine pack #s
PACKS=()
for str in "$clip"
do
  PACKS+=$(echo -e "$str" | cut -d$'\t' -f2)
done
botname=$(echo "$str" | head -1 | cut -d$'\t' -f1)
pack=$(echo $PACKS | tr ' ' ',')

clip="-s irc.rizon -c .#NIBL -m '/msg ${botname} xdcc batch ${pack}'"
clip2="-s irc.rizon -c .#nibl -m '/msg ${botname} xdcc batch ${pack}'"

echo -e "$clip"  | req_dcc
echo -e "$clip2" | req_dcc

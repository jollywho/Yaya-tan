if [[ -z $@ ]]; then
  exit
fi
red='\\e[0;31m'
yellow='\\e[0;33m'
cyan='\\e[0;36m'
green='\\e[1;32m'
NC='\\e[0m'
str=$@
m=${str// /+}
url=$(wget -q -O- http://nibl.co.uk/bots.php?search=$m | sed 's/<td class="\(botname\|packnumber\|filesize\|filename\)">/<td class="\1">\n/g')
bot="/html/body/div/div/div/table/tr/td[@class = 'botname']/text()"
pack="/html/body/div/div/div/table/tr/td[@class = 'packnumber']/text()"
size="/html/body/div/div/div/table/tr/td[@class = 'filesize']/text()"
name="/html/body/div/div/div/table/tr/td[@class = 'filename']/text()"
echo -e "$url" | xmllint --html --xpath "$bot" --format - | sed '/^\s*$/d' | sed 's/^/'"${yellow}"'/' | sed 's/\s*$/'"${NC}"'/' > a
echo -e "$url" | xmllint --html --xpath "$pack" --format - | sed '/^\s*$/d' | sed 's/^/'"${cyan}"'/' | sed 's/$/'"${NC}"'/' > b
echo -e "$url" | xmllint --html --xpath "$size" --format - | sed '/^\s*$/d' | sed 's/^/'"${red}"'/' | sed 's/$/'"${NC}"'/' > c
echo -e "$url" | xmllint --html --xpath "$name" --format - | sed '/^\s*$/d' | sed 's/^/'"${green}"'/' | sed 's/$/'"${NC}"'/' > d
o=$(paste -d "|" a b c d)
rm a b c d
echo -e "$o"

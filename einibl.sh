if [[ -z $@ ]]; then
  exit
fi
str=$@
m=${str// /+}
url=$(wget -q -O- http://nibl.co.uk/bots.php?search=$m | sed 's/<td class="\(botname\|packnumber\|filesize\|filename\)">/<td class="\1">\n/g')
bot="/html/body/div/div/div/table/tr/td[@class = 'botname']/text()"
pack="/html/body/div/div/div/table/tr/td[@class = 'packnumber']/text()"
size="/html/body/div/div/div/table/tr/td[@class = 'filesize']/text()"
name="/html/body/div/div/div/table/tr/td[@class = 'filename']/text()"
echo "$url" | xmllint --html --xpath "$bot" --format -  | sed '/^\s*$/d' > a
echo "$url" | xmllint --html --xpath "$pack" --format - | sed '/^\s*$/d' > b
echo "$url" | xmllint --html --xpath "$size" --format - | sed '/^\s*$/d' > c
echo "$url" | xmllint --html --xpath "$name" --format - | sed '/^\s*$/d' > d
paste -d "|" a b c d

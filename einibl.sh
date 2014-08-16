str=$@
m=${str// /+}
urll=$(curl -sL http://nibl.co.uk/bots.php?search=$m)
bot="/html/body/div/div/div/table/tr/td[@class = 'botname']/text()"
pack="/html/body/div/div/div/table/tr/td[@class = 'packnumber']/text()"
size="/html/body/div/div/div/table/tr/td[@class = 'filesize']/text()"
name="/html/body/div/div/div/table/tr/td[@class = 'filename']/text()"
a=$(echo $urll | xmllint --html --xpath '/html/body/div/div/div/table/tr/td[@class = 'botname']/text()' --format -)
b=$(echo $urll | xmllint --html --xpath '/html/body/div/div/div/table/tr/td[@class = 'filename']/text()' --format -)
#c=$(echo $urll | xmllint --html --xpath '$size' --format -)
#d=$(echo $urll | xmllint --html --xpath '$name' --format -)
paste <(echo "$a") <(echo "$b") -d '|'

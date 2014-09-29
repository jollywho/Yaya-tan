require 'nokogiri'
require 'open-uri'

if ARGV.size == 0
  puts "no records found"
  exit
end
aid = ARGV[0]
url = "http://api.anidb.net:9001/httpapi\?request\=anime\&client\=yaya\&clientver\=1\&protover\=1\&aid\="
req = url + aid
o = Nokogiri::XML(open(req))


f = File.open('aniout', 'w')
f.write(o)


ep = o.xpath("//episodecount")[0].content
puts(ep)

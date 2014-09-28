require 'nokogiri'
require 'open-uri'

aid = ARGV[0]
url = "http://api.anidb.net:9001/httpapi\?request\=anime\&client\=yaya\&clientver\=1\&protover\=1\&aid\="
req = url + aid
o = Nokogiri::XML(open(req)).xpath("//episodecount")[0].content
puts(o)

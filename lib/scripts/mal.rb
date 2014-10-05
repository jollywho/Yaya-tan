require 'nokogiri'
require 'open-uri'

if ARGV.size < 3
  exit
end
id = ARGV[0]
pw = ARGV[1]
aid = ARGV[2]
url = "http://myanimelist.net/api/anime/search.xml\?q\="
req = url + aid
o = Nokogiri::XML(open(req, http_basic_authentication: ["#{id}", "#{pw}"]))

ep = o.xpath("//episodes")
#date = o.xpath("//startdate")[0].content.strip
puts ep
#puts("#{ep}|#{date}")

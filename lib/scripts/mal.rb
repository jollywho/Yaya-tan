require 'nokogiri'
require 'open-uri'

if ARGV.size < 3
  exit
end
id = ARGV[0]
pw = ARGV[1]
title = ARGV[2]
url = "http://myanimelist.net/api/anime/search.xml\?q\="
req = url + title
o = Nokogiri::XML(open(req, http_basic_authentication: ["#{id}", "#{pw}"]))

title = title.upcase()
o.xpath("//title").each do |i|
  c = i.content.upcase().tr(" ", "_")
  if c == title
    t = o.xpath("//title[text()='#{i.content}']/..")
    t.each do |m|
      ep = t.css('episodes').text.strip
      sd = t.css('start_date').text.strip
      puts("#{ep}|#{sd}")
    end
  end
end


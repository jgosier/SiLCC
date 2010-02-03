# jso.rb
# This parses through json files
# Testing term extraction using Yahoo apis
require "rubygems"
require "json"

tweet_objects = []

File.open('haiti_quake_backsearch_collected_data.json','r') do |f1|
	while line = f1.gets()
		tweet_objects.push(JSON.parse(line))
	end
end

puts tweet_objects[0]['text']
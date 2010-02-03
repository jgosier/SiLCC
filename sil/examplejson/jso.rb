# jso.rb
# This parses through json files
# Testing term extraction using Yahoo apis

#require 'json'

tweets = []

File.open('haiti_quake_backsearch_collected_data.json','r') do |f1|
	while line = f1.gets()
		tweets.push(line)
	end
end

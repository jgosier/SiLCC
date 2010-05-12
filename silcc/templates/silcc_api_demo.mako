<%inherit file="silcc_base.mako"/>



<%def name="main()">
	
	<div class="left">
					<H1>ABOUT SiLCC</H1>	

					<p>SiLCC is a cloud based service for parsing text and extracting relevant keywords. To use it, you must first apply for an API key. Input the API key into your application and then push content to our server. As we receive your content, we parse it, extract relevant 'tags', then send it back to your app. From there user interaction with those tags (editing or removal) helps to improve our algorithms.</p>

					<p>SiLLC also features robust glossaries for Twitter pico-formats and SMS txtSpeak. It specializes in the semantic tagging of content that's 280 characters and less.</p>
	</div>
					
<div class="left">
						<H1>Tagging Demo</H1>
##						<DIV class="location">
##							You are here: Swift / Extend / <a href="http://www.swift.ushahidi.com/extend/">Ideas</a>
##						</DIV>                
<script type="text/JavaScript">

    function submit_text() {
        var text = $('input_text').value;
				if (!text) {
				   alert('Please enter some text to tag!');
           return;
        }
        var postdata='text='+encodeURIComponent(text);
				postdata+='&key=${c.apikey}';
        $('tag_results').innerHTML='Analysing text...<div style="text-align: center; vertical-align:center"><img src="/media/ajax-loader.gif"></div>'
				asyncLoadDiv('/api/tag', postdata, $('tag_results'));
    }

</script>
</div>
<div class="left">

<div id="formbody">
<form id="test_form" action="/api" method="post">
<table>
    <tr>
        <td class="label">Enter Text: </td>
        <td><input name="text" id="input_text"
                    size=60 
             />
        </td>
    </tr>
		<tr>
        <td></td><td><input type="submit" value="Tag it!" onclick="submit_text();return false;"></td>
    </tr>
</table>
</form>
</div>

<br/><br/><br/>
<h1>Tagger Results:</h1>

<div id="tag_results" style="height:100px"></div>

<h1>Tagging API</h1>
<p>
The above form demonstrates the tagging API. To use the API send an http POST to
the http://silcc.nrny.net/api with text encoded in a 'text' parameter.
Text should be URI encoded.
</p> 
</div>

							<BR>
							<BR>
							<BR>
							<BR>
							<BR>
							<BR><BR>
							<BR>
							<BR>
							<BR>
						
			

</%def>

<%inherit file="base_960.mako"/>

<%def name="title()">
Swift River SiLCC API
</%def>

<%def name="body()">



<div id="formbody">
<form id="test_form" action="/api" method="post">
<table>
    <tr>
        <td class="label">text: </td>
        <td><input name="text" 
                    size=60 
             />
        </td>
    </tr>
		<tr>
        <td colspan="2"><input type="submit"></td>
    </tr>
</table>
</form>

<H1>SiLLC Tagger Bookmarklet</H1>

    <div style="font-size:10pt; text-align:justify; color: gray; width:450px">
        Drag this link: <a href="javascript:location.href='http://tom:5000/api?text='+encodeURIComponent(document.title)">Tag this!</a>
        to your browser's toolbar to easily submit a title for tag extraction.<br><br>
    </div>


</div><!-- id=formbody-->
</%def>
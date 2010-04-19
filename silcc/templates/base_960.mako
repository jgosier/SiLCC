<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Swift River SiLCC API</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" media="all" href="/static/reset.css" />
<link rel="stylesheet" type="text/css" media="all" href="/static/text.css" />
<link rel="stylesheet" type="text/css" media="all" href="/static/960.css" />
<link href="/static/styles_960.css" media="screen" rel="Stylesheet" type="text/css" />
</head>
<body>
## /--------------------- * container_16 id=container * ---------------------\
## |*------------------------_grid_16 id=banner_----------------------------*|
## || logo                                                search            ||
## |*.......................................................................*|
## |*------------------------grid_16 id=navbar------------------------------*|
## || hot new top                                                           ||
## |*.......................................................................*|
## |*----------- grid_11 id=main -------------------* *- grid_5 id=sidebar -*|
## ||*grid_1**---grid_10 class=sub-----------------*| |*--user_actions-----*||
## |||      ||Title (host)                         || ||  (or login)       |||
## |||      ||by X                                 || |*-------------------*||
## |||      ||tags etc.                            || |*----adverts--------*||
## ||*------**-------------------------------------*| ||                   |||
## ||                                               | |....................*||
## ||                                               | |*------tags---------*||
## ||                                               | ||popular tags...    |||
## ||                                               | |*-------------------*||
## |*-----------------------------------------------* *---------------------*|
## |*------------------------- grid_16 id=footer ---------------------------*|
## ||                                                                       ||
## |*-----------------------------------------------------------------------*|
## \........................................................................./
<div class="container_16" id="container">

	${self.banner()}
  <div class="clear"></div>


  <div class="grid_11" id="main">
    ${self.body()}
  </div><!--main-->

  <div class="grid_5" id="sidebar">
    ##${self.sidebar()}
  </div><!--sidebar-->

  <div class="grid_16 spacer"></div>
  <div class="clear"></div>

  <div class="grid_16">${self.footer()}</div>
  <div class="clear"></div>

  ${self.jscripts()}  

</div><!--container_16-->
</body>
</html>


## -------------------------- title ----------------------------
<%def name="title()">
Swift River SiLLC API
</%def>
## -------------------------- banner ---------------------------
<%def name="banner()">
  <div class="grid_11"><img src="/static/logo.png" alt="Logo"/></div>
  <div class="grid_5">
    ##<form id="banner_search" action="/search">
    ##  <p>
    ##    <input name="search"/>
    ##    <input type="submit" value="submit"/>
    ##  </p>
    ##</form>

  </div>
</%def>
## -------------------------- navbar ---------------------------
<%def name="navbar()">
<%
    views = ('hot', 'new', 'top', 'stats', 'about', 'tools', 'more')
%>
<ul>
% for v in views:
##<li><a href="/${v}">${v}</a></li>
    % if c.view == v:
    <li><a href="/${v}" class="current_view">${v}</a></li>
    % else:
    <li><a href="/${v}">${v}</a></li>
    % endif
% endfor
</ul>
</%def>
## ------ login bar (test) ------
<%def name="loginbar()">
<form id="login">
<p>
<input name="username"><input name="password"><br>
<input type="submit">
</p>
</form>
</%def> 
## -------------- List of links/submissions for laying out links on all pages------
<%def name="render_subs()">
% for sub in c.links:
<div class="grid_1 alpha vote_box">
<p id="vb${sub['sbid']}" class="v">${sub['sbvotebal']}</p><br/>
<div><a onclick="vote(${sub['sbid']});return false" href="/vote/${sub['sbid']}">
% if c.vote_dict and c.vote_dict.get(sub['sbid'],0)==1:
<img id="v${sub['sbid']}" src="/static/upvoted.png" alt="Vote" style="border:0 none"/>
% else:
<img id="v${sub['sbid']}" src="/static/up.png" alt="Vote" style="border:0 none"/>
% endif
</a></div>
</div>

<div class="grid_10 omega sub">
<a class="l" href="${sub['sburl']}">${sub['sbtitle'].decode('utf-8','ignore')}</a>
<p class="h">(${sub['sbhost']})</p><br/>
<p class="l">by <a class="by" href="/members/${sub['sbmbname']}">${sub['sbmbname']}</a>
${human_age(sub['sbdatesbmt'])} ago.</p> <a href="/subs/${sub['sbid']}/comments" class="c">${sub['sbcomments']} comments<a>
% if sub['sbtags']:
${self.format_tags(sub['sbtags'],())}
% endif
${self.format_link_actions(sub['sbid'],sub)}
##${self.render_edit_tags_form(sub['sbid'])}
</div>

<div class="clear"></div>
% endfor
</%def>
## ------------- format tags in links ------------------------------
<%def name="format_tags(tags, user_tags)">
<div class="tags">
##% if c.username:
##<ul class="tag_actions">
##<li>add tag</li>
##<li>del tag</li>
##</ul>
##% endif
% for tag in tags.split():
<a href="/tag/${tag}">${tag}</a>
% endfor
</div>
</%def>
## ----------------- format link actions --------------------------
<%def name="format_link_actions(sbid,sub)">
<div class="link_actions">
% if c.username:
    <a href="/submissions/${sbid}/moderate">moderate</a>
% endif
% if c.admin_user:
    <a href="/submissions/${sbid}/delete">delete</a>
    <a href="/submissions/${sbid}/move_to_spam">move to spam</a>
% endif
% if c.username:
    ${self.edit_tags_forms(sbid,sub['sbtags'])}
% endif
</div>
</%def>
## ------------ Render Edit Tags Form -------------------------
<%def name="render_edit_tags_form(sbid)">
This is the tags form which will be normally hidden to start with...
</%def>
## ------------ Edit Tags Forms -------------------------------
<%def name="edit_tags_forms(sbid,tags)">

                <a href="javascript:show_edit_tags_form(${sbid});" class="sublink"
                        id="edit_tags${sbid}">add tag</a>
                <script type="text/javascript">
                    usertags[${sbid}]=${str(c.usertags.get(sbid, []))};
										% if tags:
                       tags=${tags.split()};
                    % else:
                       tags=[];
                    % endif
                </script>
                    % if c.usertags.get(sbid):
                        <a href="javascript:show_delete_tags_form(${sbid});" class="sublink"
                            id="delete_tag${sbid}">del tag</a>
                    % else:
                        <a href="javascript:show_delete_tags_form(${sbid});" style="display:none" class="sublink"
                            id="delete_tag${sbid}">del tag</a>
                    % endif
                        
                        <form id="edit_tags_form${sbid}" action="javascript:validate_tags('${sbid}');" style="display:none;" class="edit_tags_form">
                        <!--<div id="edit_tags_form$sbid" style="display:none;" class="edit_tags_form">-->
                
                <span class="error_message" style="font-size:10pt;display:none" id="edit_tags_msg${sbid}">
                    please enter your comment in the box below</span>
                <!--<form style="display:inline" action="javascript:validate_tags('$sbid');">-->
                <input name="tags" id="tags_edit_text${sbid}"></input>
                <input type="submit" value="save" class="btn" 
                onmouseover="hov(this,'btn btnhov')" onmouseout="hov(this,'btn')"
                onclick="validate_tags('${sbid}');return false;">
                <input type="submit" value="cancel" class="btn" 
                onmouseover="hov(this,'btn btnhov')" onmouseout="hov(this,'btn')"
                    onclick="hide_edit_tags_form(${sbid});return false;">
                <!--</form>-->
                <!--</div>-->
                </form>
                <div id="delete_tags_form${sbid}" 
                    style="display:none;" class="delete_tags_form">
                only tags that have been added by you may be deleted.<br>
                1) These tags have been added only by you and may be deleted.<br>
                2) One or more other people has tagged this link as well. You may
                delete your copy of the tag though<br>
              
                
                <span id="delete_tags_html${sbid}"></span>
                <input type="submit" value="delete" class="btn" 
                onmouseover="hov(this,'btn btnhov')" onmouseout="hov(this,'btn')"
                onclick="delete_tags('${sbid}');return false;">
                <input type="submit" value="cancel" class="btn" 
                onmouseover="hov(this,'btn btnhov')" onmouseout="hov(this,'btn')"
                    onclick="hide_delete_tags_form(${sbid});return false;">
                </div>


</%def> 
## ------------Format Age is nice human readable form----------
<%def name="human_age(sbdatesbmt)">
<%
		import time
		def calc_age(t):
        unix_ts = time.mktime(t.timetuple())+1e-6*t.microsecond
        secs = time.time() - unix_ts
        days = int(secs/86400)
        if days == 1: return '1 day'
        if days > 1: return '%d days' % days
        hrs = int(secs/3600)
        if hrs == 1: return '1 hour'
        if hrs > 1: return '%d hours' % hrs
        mins = int(secs/60)
        if mins == 1: return '1 minute'
        if mins > 1: return '%d minutes' % mins
        if secs == 1: return '1 second'
        return '%d seconds' % secs
%>
${calc_age(sbdatesbmt)}
</%def>
## -------------------------- login box -----------------------
<%def name="loginbox()">
<div id="login">
<h1>Login</h1>
<form action="/process_login" method="post">
<p>
<table>
<tr><td><input class="f" name="username"/></td><td><input class="f" name="password" type="password" /></td></tr>
<tr><td>Remember me?:<input type="checkbox" name="autologin"/></td><td align="right"><input type="submit" name="submit" value="Login"/></td></tr>
</table>

</p>
<p>Not a member? <a href="/register">Register here.</a></p>
</form>
<!-- This one below is a direct copy from muti old... -->
##<form name="logform" action="/process_login" method="post">
##  <p>
##		<input type="radio" name="loginOrReg" value="login" checked="checked">Login
##			<input type="radio" name="loginOrReg" value="register">Register<br>
##					Username:<br>
##						<input name="username" class="textfield" maxlength="20"><br>
##								Password:<br>
##									<input name="password" class="textfield" type="password" maxlength="20"><br>
##											<input type="checkbox" name="autologin">Auto-login<br>
##													<input type="submit" name="submit" value="login/register"><br>
##   <span class="subinfo"><a class="noul" href="/forgot_password">forgot password?</a></span>
##  </p>
##</form>

</div>
</%def>
## ---------------------------User Actions Box -----------------
<%def name="user_actions()">
<div id="user_actions">
<p id="username">Logged in as: <b>${c.username}</b></p>
<ul>
<li><a href="/submit">Submit</a></li>
<li><a href="/profile">Profile</a></li>
<li><a href="/mine">My Posts</a></li>
<li><a href="/saved">Saved</a></li>
<li><a href="/liked">Liked</a></li>
<li><a href="/moderated">Moderated</a></li>
##<li><a href="/friends">Friends</a></li>
##<li><a href="/friends_posts">Friends Posts</a></li>
##<li><a href="/followers">Followers</a></li>
##<li><a href="/hidden">Hidden Users</a></li>
<li><a href="/process_logout">Log Out</a></li>
</ul>
</div>
</%def>
## -------------------------- Sidebar --------------------------
<%def name="sidebar()">
% if c.username:
${self.user_actions()}
% else:
${self.loginbox()}
% endif
${self.adverts()}
% if c.tags:
<div id="tags">
<h1>Popular Tags</h1>
<ul>
% for tag in c.tags:
<li><a href="/tag/${tag['tgtag']}">${tag['tgtag']}</a></li>
% endfor
</ul>
</div>
% endif
</%def>
## -------------------------- Adverts --------------------------
<%def name="adverts()">
<div id="adverts">
<h1>SPONSORED LINKS</h1>
##<script type="text/javascript"><!--
##google_ad_client = "pub-3531753547734305";
##/* 125x125, created 1/9/10 for New Muti left */
##google_ad_slot = "4016472820";
##google_ad_width = 125;
##google_ad_height = 125;
##//-->
##</script>
##<script type="text/javascript"
##src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
##</script>
<img src="/static/sa_rocks_125_ad.gif" alt="SA Rocks"/>
<img src="/static/sa_rocks_125_ad.gif" alt="SA Rocks"/>
<img src="/static/sa_rocks_125_ad.gif" alt="SA Rocks"/>
<img src="/static/sa_rocks_125_ad.gif" alt="SA Rocks"/>
</div><!-- adverts -->
</%def>
## -------------------------- footer ---------------------------
<%def name="footer()">
<div id="footer">
    <a class="banneraction" href="/about">About</a>&nbsp;|
    <a class="banneraction" href="/terms">Terms of Use</a>&nbsp;|
    <a class="banneraction" href="/whatsnew">What's&nbsp;new?</a>&nbsp;|
    <a class="banneraction" href="/feedback">Feedback</a>&nbsp;|  
    <a class="banneraction" href="/static/newsmap.html">Newsmap</a><br>
##    Hosting Sponsored by: <a href="http://www.wantitall.co.za" style="color:#ec9601;text-decoration:none">WantItAll - For SA's best Online Shopping</a><br>
##    <a href="http://www.wantitall.co.za"><img src="/static/wantitall.gif" height="45" border="0" alt="wantitall"></a>
</div>
</%def>
## -------------------------- jscripts -------------------------
<%def name="jscripts()">
<script src="/static/jquery-1.3.min.js" charset="utf-8"></script>
<script src="/static/scripts.js" charset="utf-8"></script>
</%def>

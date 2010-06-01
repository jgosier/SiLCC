<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<HTML xmlns="http://www.w3.org/1999/xhtml" lang="en">
	<HEAD>
			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">					
		    <title>Swiftriver | Verifying and Filtering News (FOSS)</title>
		    <meta name="description" content="Swiftriver is a free and open source software platform that uses a combination of algorithms and crowdsourced interaction to validate and filter news. It is an open source effort by many contributing people and organizations including Meedan, Appfrica, GeoCommons and Ushahidi.">
		    <meta name="keywords" content="journalism, crisis, verify, filter, news, emergency, rank">
		    <meta name="copyright" content="Ushahidi - 2010">
		    <meta name="author" content="Ushahidi">
		    <meta name="email" content="info@ushahidi.com">
		    <meta name="Charset" content="UTF-8">
		    <meta name="Distribution" content="Global">
		    <meta name="Rating" content="General">
		    <meta name="Robots" content="INDEX,FOLLOW">
		    <meta name="Revisit-after" content="1 Day">
		    <meta name="expires" content="never">
		    <link href="media/swift/style.css" rel="stylesheet" type="text/css" />
			<script type="text/JavaScript" src="media/swift/curvycorners.js"></script>
			<script type="text/JavaScript" src="media/scripts.js"></script>
			<script type="text/JavaScript">

			  addEvent(window, 'load', initCorners);

			  function initCorners() {
			    var settings = {
			      tl: { radius: 5 },
			      tr: { radius: 5 },
			      bl: { radius: 5 },
			      br: { radius: 5 },
			      antiAlias: true
			    }

			    /*
			    Usage:

			    curvyCorners(settingsObj, selectorStr);
			    curvyCorners(settingsObj, Obj1[, Obj2[, Obj3[, . . . [, ObjN]]]]);

			    selectorStr ::= complexSelector [, complexSelector]...
			    complexSelector ::= singleSelector[ singleSelector]
			    singleSelector ::= idType | classType
			    idType ::= #id
			    classType ::= [tagName].className
			    tagName ::= div|p|form|blockquote|frameset // others may work
			    className : .name
			    selector examples:
			      #mydiv p.rounded
			      #mypara
			      .rounded
			    */
			    curvyCorners(settings, "#myBox1, #myBox2, #myBox3, #myBox4");
			  }

			</script>
	</HEAD><BODY>
		<div id="top">
			<p>
				<ul>
					<li class="version" >v0.1 Apala</li>
					<li class="link" ><a href="http://swift.ushahidi.com" title="overview" >About SwiftRiver</a></li>
					<li class="link" ><a href="https://spreadsheets.google.com/a/ushahidi.com/viewform?hl=en&formkey=dHB2X3ZZSUZYTVJ0RnlFbFg2SElzQ3c6MA" title="download" >Get Swift</a></li>
					<li class="link" ><a href="http://swift.ushahidi.com/doc/" title="notes on use, features and api" >Documentation</a></li>
					<li class="link" ><a href="http://github.com/appfrica/silcc/" title="developers" >Developers</a></li>
					<li class="link" ><a href="http://swift.ushahidi.com/doc/doku.php?id=faq" title="frequently asked questions" >FAQ</a></li>
					<li class="link" ><a href="http://swift.ushahidi.com/goodies/" title="goodies" >Goodies</a></li>
				</ul>
			</p>
		</div>
		<DIV class="big_wrapper_1">
			<DIV class="wrapper_1">
				<a href="http://www.swift.ushahidi.com/"><img class="logo" src="media/swift/logo1.png" alt="swiftriver logo" /></A>			
				<P>
					<A href="http://swift.ushahidi.com/" class="me" class="first" title="home">HOME</A>
					<A href="http://blog.ushahidi.com/index.php/category/swift-river/" title="blog">BLOG</A>					
					<A href="http://www.ushahidi.com/contact" title="contact us">CONTACT</A>
					<A href="#events" title="events">EVENTS</A>
					<A href="http://swift.ushahidi.com/extend/" title="extend swift">EXTEND</A>
				</P>
			</DIV>
		</DIV>
		
		<DIV class="big_wrapper_2">
			<DIV class="wrapper_2">
				<DIV class="content">
    ${self.main()}

								<div class="right">							
									<div class="column_holder" style="">
										<div id="myBox1" >
											<H3 class="pt17">Community</H3>
											<p>Join the discussion on the curation and validation of real-time news. Connect with us on Twitter <strong><a href="http://twitter.com/swiftriver">@swiftriver</a></strong>, our <strong><a href="http://groups.google.com/group/swiftriver">Google Group</a></strong>, our <strong><a href="http://www.skype.com/go/joinpublicchat?skypename=j%2egosier&topic=Swift%20River%20Public&blob=fCcfQEJLCSTkdNTZb_N-1VUtFLMZ2WuCz2GtImXrKhwbSyUPnxeiIRKVwVjKIbnPDvgwmo-jdd-9LmLRVuL7NHFgx72WyehIWwwPgAEhNi1um9TsYckFFcqPctFtxhshooxnZ6MrUUVNj7gpAcOF-9ELLMG1_IEq5myJBMlyVSC07bZT-cf9k6tqLMC5Ar0DFQ">Skype Chat</a></strong>, or on <strong><a href="http://www.facebook.com/pages/Swiftriver/362720609137">Facebook</a></strong>.</p>
										</div></div>						
			                        <div class="column_holder" style="">
										<div id="myBox2" >
											<div id="developer"><H3 class="pt17">Developers</H3></div>
											<P>SiLCC is an open source project. We invite anyone interested in working with us to join our developer community by following us on <a href="http://github.com/appfrica/silcc">Git Hub</a>.
			                                </P>
										</div>
			                        </div>
									<div class="column_holder" style="">
										<div id="myBox3" >
			                            	<H3 class="pt17">Swift River Research</H3>
												A curated collection of most of the research that went into developing SwiftRiver. <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Veracity_and_Validation_030582_8676078002899885">Veracity and Validation</A>, <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Authority_and_Trust_7665742095_30467821657657623">Authority and Trust</A>, <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Predictive_Tagging">Predictive Tagging</A>, <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Community_Curation">Community Curation</A>, <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Taxonomy_and_Picoformats">Taxonomy and Picoformats</A>, <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Visualization_Methods_11566399_23362584318965673">Visualization Methods</A>, <A href="https://docs.google.com/View?docID=0AXtjM3UhUoCeZGZ0azVwYjdfMTBkZ2Q4OGtmMg&revision=_latest&hgd=1#Collected_Code">Collected Code</A>, <a href="https://docs.google.com/leaf?id=0B3tjM3UhUoCeOTNkZGIyNzYtM2M5MS00OGM3LTg0NTgtOTUzM2QyNTk1OGQ4&hl=en">System Design Documents</a>
										</div>
									</div>
									<div class="column_holder" style="">
										<div id="myBox4" >
											<div id="extend"><H3 class="pt17">Extend SwiftRiver</H3></div>
											<P>SwiftRiver is a highly extensible and modular software platform. There are two ways of extending SwiftRiver: via the API or with plugins.  Visit the <a href="http://swift.ushahidi.com/extend">Extend</a> page for details.
			                                </P>
										</div>
			                        </div>
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
										<br />
									</div>						
								</div>
							</div>
						</div>


					<div class="big_wrapper">
						<div class="wrapper">
							<div class="footer">
								<div class="footer-column">
			                	<H5>Here</H5>
			                    <UL>
			                        <li class="first"><A href="http://swift.ushahidi.com/">HOME</A></li>
			                        <li><A href="http://www.ushahidi.com/">USHAHIDI</A></li>
			                        <li><A href="http://blog.ushahidi.com/">BLOG</A></li>
			                        <li><A href="http://www.ushahidi.com/sitemap">SITEMAP</A></li>
			                        <li><A href="http://www.ushahidi.com/contact">CONTACT</A></li>
			                    </UL>
			                </div>
							</div>
						</div>
		</DIV>
		<!-- GA Tracking -->
##<SCRIPT type="text/javascript">
##	var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
##	document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
##</SCRIPT><SCRIPT src="./media/ga.js" type="text/javascript"></SCRIPT>
##<SCRIPT type="text/javascript">
##	try {
##	var pageTracker = _gat._getTracker("UA-12063676-11");
##	pageTracker._trackPageview();
##	} catch(err) {}
##</SCRIPT>
</BODY></HTML>
## ------ Body, override this in sub-templates ------
<%def name="main()">
This is the body...
</%def> 

function makeHandleOnReadyStateChange(XmlHttp,div) {
	return function() {
		if (XmlHttp.readyState == 4) {
			if (XmlHttp.status == 200) {
				$(div).innerHTML=XmlHttp.responseText;
			}
		}
	}
}

function makeResponseFunction(XmlHttp,func) {
	return function() {
		if (XmlHttp.readyState == 4) {
			if (XmlHttp.status == 200) {
				func(XmlHttp)
			}
		}
	}
}


function asyncLoadDiv(url,postdata,div) {
	this.req=getRequestObj();
	if (this.req) {
		if (div!=null) {
			this.req.onreadystatechange = makeHandleOnReadyStateChange(this.req,div);
		}
		this.req.open("POST", url, true);
		this.req.setRequestHeader('Content-Type',
			'application/x-www-form-urlencoded');
		this.req.send(postdata);
	}
}

function ajax(url,postdata,returnFunc) {
	this.req=getRequestObj();
	if (this.req) {
		if (returnFunc!=null) {
			this.req.onreadystatechange = makeResponseFunction(this.req,returnFunc);
		}
		this.req.open("POST", url, true);
		this.req.setRequestHeader('Content-Type',
			'application/x-www-form-urlencoded');
		this.req.send(postdata);
	}
}

function getRequestObj() {
	req = false;
	if(window.XMLHttpRequest) {
		try {
			req = new XMLHttpRequest();
		} catch(e) {
			req = false;
		}
	}
	else
		if(window.ActiveXObject) {
			try {
				req = new ActiveXObject("Msxml2.XMLHTTP");
			} catch(e) {
				try {
					req = new ActiveXObject("Microsoft.XMLHTTP");
				} catch(e) {
					req = false;
				}
			}
		}
	return req
}

function $() {
	var elements = new Array();
	for (var i = 0; i < arguments.length; i++) {
		var element = arguments[i];
		if (typeof element == 'string')
			element =
				document.getElementById(element);
		if (arguments.length == 1)
			return element;
		elements.push(element);
	}
	return elements;
}

function tagger_return() {
  alert('back from ajax!');
}
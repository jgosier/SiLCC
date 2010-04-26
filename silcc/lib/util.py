import re

url_re = re.compile('''
    ^             # we should strip the url first of leading whitespace
    (?:           # non capturing group
    http          # protocols...
    |ftp
    |file
    |mailto
    |gopher
    |news
    |https
    |wais) 
    ://          # protocol / host separator
    (?:www.)?    # we are not interested in leading 'www.' if there...
    ([^:/]*)     # everything up to the first : or / is the host name
    .*           # rest of the url
''', re.VERBOSE | re.IGNORECASE)

def get_host(sburl):
    s = url_re.search(sburl)
    if s:
        sbhost = s.group(1)
    else:
        sbhost = ''    # did not match url regex
    return sbhost


class CIList(list):
    '''
    Case Insensitive list
    A simple derivation of standard list with the
    in operator overridden to make comparisons
    case insensitive.
    '''
    def __contains__(self, key):
        for t in self:
            if key.lower() == t.lower():
                return True
        return False


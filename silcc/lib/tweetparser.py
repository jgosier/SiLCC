import re
import sys

from silcc.lib.tweettokenizer import TweetTokenizer

class ParserException(Exception):
    '''
    Raise if the parser fails to parse the tweet
    '''
    pass

class TweetParser(object):
    '''
    Tweets consist of text, with possible @names and #tags
    in the text, and possible list of #tags at end of text.
    In addition they can also contain urls.
    We will parse the tweet out into four sections:

    1) Text. This is the actual text in the tweet with
    any embedded hashtags converetd to normal words.
    Urls will be excluded and any hashtags at the end
    of the text will be excluded. In addition 
    commas, quotes, parens and other punctuation are 
    stripped out.

    2) urls. A list of any urls in the tweet

    3) hashtags. List of hashtags within the tweet 
    in the order that they appeared.

    4) @names. List of @names in the tweet in order 
    that they appeared. 
    '''

    def append_word(current_state, D, token, next_state):
        '''
        Adds a WORD token to the text list.
        '''
        text = D.get('text', [])
        if not text:
            D['text'] = [token[1]]
        else:
            text.append(token[1])


    def append_hashtag(current_state, D, token, next_state):
        '''
        Adds a HASHTAG token to the hashtag list.
        '''
        hashtags = D.get('hashtags', [])
        if not hashtags:
            D['hashtags'] = [token[1]]
        else:
            hashtags.append(token[1])

    def append_taggroup(current_state, D, token, next_state):
        '''
        Adds a HASHTAG token to the current tag group.
        '''
        taggroup = D.get('taggroup', [])
        if not taggroup:
            D['taggroup'] = [token[1]]
        else:
            taggroup.append(token[1])


    def append_name(current_state, D, token, next_state):
        '''
        Adds a @NAME token to the names list.
        '''
        names = D.get('names', [])
        if not names:
            D['names'] = [token[1]]
        else:
            names.append(token[1])

    def flush_taggroup(current_state, D, token, next_state):
        '''
        Flushes tag group to the text attribute
        when the next token is not also a hashtag.
        '''
        hashtags = D.get('hashtags', [])
        if not hashtags:
            D['hashtags'] = D['taggroup'][:]
        else:
            hashtags += D['taggroup'][:]
        del D['taggroup']


    def flush_taggroup_append_name(current_state, D, token, next_state):
        '''
        Flushes tag group to the hashtags attribute
        and appends the @name token to the names.
        '''
        hashtags = D.get('hashtags', [])
        names = D.get('names', [])
        # First append the name to the names
        if not names:
            D['names'] = [token[1]]
        else:
            names.append(token[1]) 
        # Now flush the taggroup to the hashtags...
        if not hashtags:
            D['hashtags'] = D['taggroup'][:]
        else:
            hashtags += D['taggroup'][:]
        del D['taggroup']


    def flush_taggroup_append_word(current_state, D, token, next_state):
        '''
        Flushes tag group to the text attribute
        and appends the word to the text.
        '''
        text = D.get('text', [])
        hashtags = D.get('hashtags', [])
        if not text:
            # First copy all the hashtags to text sans the '#'
            text = [t[1:] for t in D['taggroup']]
            # Now add the current token
            text.append(token[1])
            D['text'] = text
        else:
            text += [t[1:] for t in D['taggroup']]
            text.append(token[1])
        # Now also add all the tags in the tagggroup
        if not hashtags:
            D['hashtags'] = D['taggroup'][:]
        else:
            hashtags += D['taggroup'][:]
        del D['taggroup']

    def append_url(current_state, D, token, next_state):
        '''
        Appends a url token to the urls.
        '''
        urls = D.get('urls', [])
        if not urls:
            D['urls'] = [token[1]]
        else:
            urls.append(token[1])

    #      STATE          TOKEN          ACTION               NEXT_STATE  
    parse_rules = (
        ( 'START',       'WORD',         append_word,         'TEXT' ),
        ( 'START',       '#TAG',         append_taggroup,     'TAGGROUP' ),
        ( 'TEXT',        'DOLLARS',      append_word,         'TEXT'),
        ( 'START',       '@NAME',        append_name,         'TEXT'),
        ( 'START',       'RT',           None,                'START'), 
        ( 'START',       'LEFT_PAREN',   None,                'START'), 
        ( 'START',       'RIGHT_PAREN',  None,                'START'), 
        ( 'START',       'DOTS',         None,                'START'), 
        ( 'START',       'OTHER',        None,                'START'),
        ( 'START',       'URL',          append_url,          'TEXT'),
        ( 'START',       'COLON',        None,                'TEXT'),  
        ( 'START',       'HALFWORD',     None,                'TEXT'),  
        ( 'START',       'PERCENTAGE',   None,                'START'),
        ( 'TEXT',        'WORD',         append_word,         'TEXT'),
        ( 'TEXT',        '@NAME',        append_name,         'TEXT'),
        ( 'TEXT',        'URL',          append_url,          'TEXT'),
        ( 'TEXT',        'COLON',        None,                'TEXT'),
        ( 'TEXT',        'COMMA',        None,                'TEXT'),  
        ( 'TEXT',        'DOLLARS',      append_word,         'TEXT'),
        ( 'TEXT',        'QMARK',        None,                'TEXT'),
        ( 'TEXT',        'PERCENTAGE',   None,                'TEXT'),
        ( 'TEXT',        'LEFT_PAREN',   None,                'TEXT'),
        ( 'TEXT',        'RIGHT_PAREN',  None,                'TEXT'),
        ( 'TEXT',        'DOTS',         None,                'TEXT'),
        ( 'TEXT',        'OTHER',        None,                'TEXT'), 
        ( 'TEXT',        'EXCLAIM',      None,                'TEXT'),
        ( 'TEXT',        'HALFWORD',     None,                'TEXT'), 
        ( 'TEXT',        'RT',           None,                'TEXT'),
        ( 'TEXT',        'EMOTICON',     None,                'TEXT'),
        ( 'TEXT',        '#TAG',         append_taggroup,     'TAGGROUP'),
        #( 'TAGGROUP',    'COLON',        flush_taggroup,      'TEXT'),
        ( 'TAGGROUP',    'COLON',        None,                'TAGGROUP'),
        ( 'TAGGROUP',    'WORD',         flush_taggroup_append_word,  'TEXT'),
        ( 'TAGGROUP',    '@NAME',        flush_taggroup_append_name,  'TEXT'),  
        ( 'TAGGROUP',    '#TAG',         append_taggroup,     'TAGGROUP' ),
        ( 'TAGGROUP',    'DASHES',       None,                'TAGGROUP'),
        ( 'TAGGROUP',    'LEFT_PAREN',   None,                'TAGGROUP'),
        ( 'TAGGROUP',    'RIGHT_PAREN',  None,                'TAGGROUP'),
        ( 'TAGGROUP',    'DOTS',         None,                'TAGGROUP'),
        ( 'TAGGROUP',    'COMMA',        None,                'TAGGROUP'),
        ( 'TAGGROUP',    'QMARK',        None,                'TAGGROUP'),
        ( 'TAGGROUP',    'EXCLAIM',      None,                'TAGGROUP'),
        ( 'TAGGROUP',    'RT',           None,                'TAGGROUP'),
        ( 'TAGGROUP',    'URL',          append_url,          'TAGGROUP'),
        ( 'TAGGROUP',    'OTHER',        None,                'TAGGROUP'), 
        )


    @classmethod
    def parse(cls, text, debug=True):
        D = dict()
        STATE = 'START'
        tokens, remainder = TweetTokenizer.scanner.scan(text)
        for t in tokens:
            current_token = t
            found_rule = False
            for r in cls.parse_rules:
                if r[0] == STATE and r[1] == current_token[0]:
                    found_rule = True
                    if debug:
                        print 'Applying: State:%s Token:%s Action:%s Next State:%s to token %s' % (r[0], r[1], r[2], r[3], current_token[1])
                    callback = r[2]
                    next_state = r[3]
                    if callback:
                        callback(STATE, D, current_token, next_state)
                    STATE = next_state
                    break
            if not found_rule:
                print text
                print '******* NO rule for token:%s state: %s' % (current_token, STATE)
                raise ParserException
        # Now join the text back into a string...
        D['text'] = ' '.join(D.get('text',[]))
        # If there are any taggroups left then we add those to the hashtags...
        taggroup = D.get('taggroup')
        if taggroup:
            hashtags = D.get('hashtags', [])
            hashtags += taggroup
            D['hashtags'] = hashtags
        return D


if __name__ == '__main__':
    tweet_text = sys.argv[1]
    tp = TweetParser()
    print tweet_text
    parsed = tp.parse(tweet_text)
    print parsed

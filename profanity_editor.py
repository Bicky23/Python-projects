import urllib.request

def check_profanity(text_to_check):
    # connects to the internet
    with urllib.request.urlopen('https://www.wdyl.com/profanity?q='+ text_to_check) as response:
        html = response.read()
    connection.close()

    if 'true' in output:
        print('Profanity Alert!!')
    elif 'false' in output:
        print('No curse words present')
    else:
        print('Cannot scan the document properly')


def read_text():
    quotes = open('text.txt')
    contents = quotes.read()
    print(contents)
    quotes.close()
    print(check_profanity(contents))


read_text()

import os


def get_video(output=None, filename=None, url=None):
    #shell = 'you-get --debug -o {} -O "{}" {}'.format(output, filename.replace(' ', ''), url)
    shell = 'you-get -o {} {}'.format(output, url.replace('&', '("&")'))
    os.system(shell)
    print('{} is done'.format(filename))

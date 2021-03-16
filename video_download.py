import os

def get_video(output, filename, url):
    shell = 'you-get --debug -o {} -O "{}" {}'.format(output, filename.replace(' ', ''), url)
    os.system(shell)
    print('{} is done'.format(filename))
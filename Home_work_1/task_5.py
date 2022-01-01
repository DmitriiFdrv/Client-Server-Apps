#  task_5
import subprocess

import chardet

urls = ['yandex.ru', 'youtube.com']

for url in urls:
    ping_url = subprocess.Popen(('ping', url), stdout=subprocess.PIPE)

    for i, line in enumerate(ping_url.stdout):
        output = chardet.detect(line)
        line = line.decode(output['encoding']).encode('UTF-8')
        print(line.decode('UTF-8')) if i < 5 else ping_url.kill()
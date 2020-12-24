from gevent import monkey
import gevent
import urllib.request

# 有IO才做时需要这一句
monkey.patch_all()


def my_downLoad(file_name, url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()

    with open(file_name, "wb") as f:
        f.write(data)

    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(my_downLoad, "1.mp4",
                 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'),
    gevent.spawn(my_downLoad, "2.mp4",
                 'http://vjs.zencdn.net/v/oceans.mp4'),
])

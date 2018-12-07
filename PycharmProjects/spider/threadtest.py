import threading
from threadpool import *
#
# def test():
#     print(1)
#
#
#
# for i in range(10):
#     t = threading.Thread(target=test)
#     t.start()
def p(a):
    print(get(a))
tu = [({'2':1},{'3':2}),({'4':2},{'5':1})]
pool = ThreadPool(5)
requests = makeRequests(p,tu)
[pool.putRequest(req) for req in requests]
pool.wait()
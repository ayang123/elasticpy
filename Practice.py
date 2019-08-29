import time
from datetime import datetime
#import pip
from time import struct_time


from elasticsearch import Elasticsearch

#try:
#    __import__(elasticsearch)
#   print("Elasticsearch imported")
#except ImportError:
#    pip.main(['install', elasticsearch])
#   print("installing Elasticsearch")

print("Time.Time() = ", time.time())
print("Time.gmtime() = ", time.gmtime())

gmtime = time.gmtime()
timeString = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime)
print("STRFTIME = ", timeString)

formatStr = "%Y-%m-%dT%H:%M:%S.%fZ"

dt = datetime.now()
print(repr(dt))
datetimeString = datetime.strftime(dt, formatStr)
print("datetime string = ", datetimeString)

datetimeString2 = "2019-08-26T13:13:13.456Z"
print("datetime string 2 = ", datetimeString2)
dt2 = datetime.strptime(datetimeString2, formatStr)
print(repr(dt2))

datetimeNow = datetime.now()
time.sleep(5)
datetimeFuture = datetime.now()

epoch = datetime.utcfromtimestamp(0)
nowSeconds = (datetimeNow - epoch).total_seconds()
futureSeconds = (datetimeFuture - epoch).total_seconds()
print(futureSeconds - nowSeconds)

#es = Elasticsearch()

#res = es.search(index="twitter", body={"query": {"range": {"time": {"gte": timeString}}}})
#print(res['hits'])





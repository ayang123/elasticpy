import time
import pip
from elasticsearch import Elasticsearch

#try:
#    __import__(elasticsearch)
#   print("Elasticsearch imported")
#except ImportError:
#    pip.main(['install', elasticsearch])
#   print("installing Elasticsearch")

print("Time.Time() = ", time.time())

print("Time.gmtime() = ", time.gmtime())

timeString = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
print("STRFTIME = ", timeString)

es = Elasticsearch()

res = es.search(index="twitter", body={"query": {"range": {"time": {"gte": timeString}}}})
print(res['hits'])





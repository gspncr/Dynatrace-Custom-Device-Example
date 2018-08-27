import requests, time, sched, random, os, ssl, random, logging, socket
from random import randint

DT_API_URL = '';
DT_API_TOKEN = '';
logging.basicConfig(filename='rasp.log',level=logging.INFO,format='%(asctime)s %(message)s')
HOST = "gallery.gspncr.com"
logging.info(HOST)
logging.info(socket.gethostbyname(HOST))

tsdef = {
	"displayName" : "Random Number A",
	"ipAddresses" : ['10.154.0.2', socket.gethostbyname(HOST)],
	"unit" : "Count",
	"dimensions": [
	],
	"types": [
		"MacbookPro"
	]
};

r = requests.put(DT_API_URL + '/api/v1/timeseries/custom:MacbookPro.random.numberA/?Api-Token=' + DT_API_TOKEN, json=tsdef);
logging.info(r);

tsdef2 = {
	"displayName" : "Random Number B",
	"ipAddresses" : ['10.154.0.2', socket.gethostbyname(HOST)],
	"unit" : "Count",
	"dimensions": [
	],
	"types": [
		"MacbookPro"
	]
};

r = requests.put(DT_API_URL + '/api/v1/timeseries/custom:MacbookPro.random.numberB/?Api-Token=' + DT_API_TOKEN, json=tsdef2);
logging.info(r);

def getRandom():
 x = (randint(1, 100))
 logging.info (x)
 return x

scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
	scheduler.enter(30, 1, print_event, ('first',))
	logging.info("Send metric");
	payload = {
     "displayName" : "MacbookPro",
     "ipAddresses" : ['10.154.0.2', socket.gethostbyname(HOST)],
     "listenPorts" : [80, 443],
     "type" : "MacbookPro",
     "favicon" : "http://www.clker.com/cliparts/E/6/d/G/w/P/gray-apple-ever-md.png",
	 "configUrl" : "https://agt19276.dev.dynatracelabs.com/#hosts/hostdetails;id=HOST-6104DF0CAE2095B9;gtf=l_2_HOURS",
     "properties" : {
		"manufacturer" : "Dynatrace LLC",
		"schedule" : "30secs",
	 },
     "series" : [
        { "timeseriesId" : "custom:MacbookPro.random.numberA",
		  "dimensions" : {
		  },
		  "dataPoints" : [ [ int(time.time() * 1000)  , getRandom() ] ]
		},
		{ "timeseriesId" : "custom:MacbookPro.random.numberB",
		  "dimensions" : {
		  },
		  "dataPoints" : [ [ int(time.time() * 1000)  , getRandom() ] ]
		}
	]};
	try:
		r = requests.post(DT_API_URL + '/api/v1/entity/infrastructure/custom/MacbookPro?Api-Token=' + DT_API_TOKEN, json=payload);
		logging.info("response: ");
		logging.info(r);
	except ssl.SSLError:
		logging.info("SSL Error");
logging.info("START")
# Within this example a Python scheduler is used to trigger a metric update every minute.
# To ensure the reliable execution of the script in a real world scenario you could either use a cron job
# or execute the script within a managed execution environment.
scheduler.enter(1, 1, print_event, ('first',))
scheduler.run()

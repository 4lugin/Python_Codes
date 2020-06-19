import threading
import urllib
import time, http.client


sleepTime = 1
hostname = input(">> hostname?(ex.1.1.1.1): ")
cNum = int(input(">> Total Send Packet?: "))
sleepTime = int(input(">> Send Packet Count Per Second: "))


start = time.time()
params = []
params = urllib.parse.urlencode(params)
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain",
    "User-agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.3; Trident/7.0; .NET4.0E; .NET4.0C)",
    "Cache-Control": "no-cache, must-revalidate"
}

count = 1
def fetch_url(url):
    global count
    try:
        conn = http.client.HTTPConnection(url,timeout=1/sleepTime)
        conn.request("GET", "/index.php", params, headers)
        time.sleep(1/sleepTime)
        conn.close()
        print ("\n"+time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
        print ("Packet Count:",count,"(Connect Success!!)")
        count = count +1

    except:
        print ("\n"+time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
        print ("Packet Count:",count,"(Not Connect)")
        count = count +1


n=1
while (n < cNum+1):
    fetch_url(hostname)
    n=n+1


print ("\nRunning Time: %s" % (time.time() - start))

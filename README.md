# Benchmark | node | python VS FPC (Lazarus-Delphi) servers



[My Youtube Channel](https://www.youtube.com/channel/UC40vkVRoZ4vWl5E-wsDhKfQ)


Benchmark test for FPC (lazarus-delphi) servers with mormot and brook frameworks against node and python (flask).

### wrk - a HTTP benchmarking tool

[wrk](https://github.com/wg/wrk) wrk is a modern HTTP benchmarking tool capable of generating significant load when run on a single multi-core CPU. It combines a multithreaded design with scalable event notification systems such as epoll and kqueue.


### Framework Brook

> [Brook](https://github.com/risoflora/brookframework) is a cross-platform microframework which helps to develop web Pascal applications built by Delphi or Lazarus IDE and Free Pascal. Its core has been developed using the Sagui library, that's why it is so fast, compact and useful to run on embedded systems.

- ##### Test Result
```
~$ wrk -t20 -c400 -d30s http://localhost:35541
Running 30s test @ http://localhost:35541
  20 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.11ms    1.61ms  86.71ms   89.68%
    Req/Sec     4.93k   423.57     7.65k    71.15%
  2952298 requests in 30.07s, 363.20MB read
Requests/sec:  98170.39
Transfer/sec:     12.08MB
```

### Framework MORMOT2

> [MORMOT2](https://github.com/synopse/mORMot2) mORMot is an Open Source Client-Server ORM SOA MVC framework for Delphi 6 up to the latest Delphi and FPC revisions, targeting Windows/Linux for servers, and any platform for clients (including mobile or AJAX).


- ##### Test Result
```
~$ wrk -t20 -c400 -d30s http://localhost:8888
Running 30s test @ http://localhost:8888
  20 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.11ms  698.32us  26.64ms   85.35%
    Req/Sec     9.59k     1.28k   19.71k    63.69%
  5733603 requests in 30.08s, 781.92MB read
Requests/sec: 190629.72
Transfer/sec:     26.00MB

```

### NODE server


```
const http = require('http');

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('<h1>pong</h1>');
}

const server = http.createServer(requestListener);
server.listen(9001);
```

- ##### Test Result
```
~$ wrk -t20 -c400 -d30s http://localhost:9001
Running 30s test @ http://localhost:9001
  20 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     7.42ms    2.30ms  83.90ms   93.19%
    Req/Sec     2.73k   272.65     5.82k    86.66%
  1636125 requests in 30.08s, 240.29MB read
Requests/sec:  54393.35
Transfer/sec:      7.99MB

```

### Python server
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Pong</h1>"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=9002)
```

- ##### Test Result
```
~$ wrk -t20 -c400 -d30s http://localhost:9002
Running 30s test @ http://localhost:9002
  20 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    22.00ms   19.68ms 950.72ms   98.77%
    Req/Sec   754.90    316.92     3.32k    80.26%
  134779 requests in 30.10s, 18.89MB read
Requests/sec:   4477.74
Transfer/sec:    642.81KB

```

# Conclusion:
We can see the test result of each http server and how mormot wins the challenge, fpc mormot is 3 times faster than node and 2 times faster than fpc Brook, http server with python is the slowest based on the result. please contact me with any suggestions to improve any of these servers and thank you.
email: i.belarouci@gmail.com.





const http = require('http');

const requestListener = function (req, res) {
  res.writeHead(200);
  res.end('<h1>pong</h1>');
}

const server = http.createServer(requestListener);
server.listen(9001);
console.log("Server running on localhost:9001");

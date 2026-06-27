// Simple Executor Gateway for Epic Agent Fabric
// This is a minimal version that works out of the box

const http = require('http');

const PORT = process.env.PORT || 8787;

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');
  
  if (req.url === '/' || req.url === '/health') {
    res.writeHead(200);
    res.end(JSON.stringify({
      status: "healthy",
      service: "Executor Gateway",
      version: "1.0.0",
      message: "Epic Agent Fabric Executor is running"
    }));
  } else if (req.url === '/connectors') {
    res.writeHead(200);
    res.end(JSON.stringify({
      connectors: ["redis", "stripe", "groq"],
      message: "These are example connectors"
    }));
  } else {
    res.writeHead(404);
    res.end(JSON.stringify({ error: "Not found" }));
  }
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`Executor Gateway running on port ${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
});

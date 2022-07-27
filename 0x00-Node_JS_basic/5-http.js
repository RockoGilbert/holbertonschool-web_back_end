const http = require('http');
const countStudents = require('./3-read_file_async.js');
const fs = require('fs');

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      //  const data = fs.readFileSync('3-read_file_async.js', 'utf-8',);

      countStudents('database.csv');

      // console.log(data)
      // res.end(`${students.join('\n')}`);
    } catch (error) {
      res.end(error.message);
    }
  }
  res.statusCode = 404;
  res.end();
});

app.listen(1245);
module.exports = app;

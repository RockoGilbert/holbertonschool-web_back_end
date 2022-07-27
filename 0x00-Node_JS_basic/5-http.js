const http = require('http');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const DATABASE = process.argv[2];

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  const { url } = req;

  if (url === '/') 
    res.write('Hello Holberton School!');

  if (url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const returnValue = await countStudents(DATABASE);
      // res.end(`${returnValue.students.join('\n')}`);
      res.write(`Number of students: ${returnValue.students.length}\n`);
      res.write(
        `Number of students in CS: ${
          returnValue.studentsByCS.length
        }. List: ${returnValue.studentsByCS.join(", ")}\n`
      );
      res.write(
        `Number of students in SWE: ${
          returnValue.studentsBySWE.length
        }. List: ${returnValue.studentsBySWE.join(", ")}`
      );
    } catch (error) {
      res.statusCode = 404;
      res.end(error.message);
    }
  }
  res.end();
});

app.listen(port, hostname, () => {
  //   res.write(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;

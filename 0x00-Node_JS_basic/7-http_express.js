const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app
.get('/', (req, res) => res.send('Hello Holberton School!'))
.get('/students', async (req, res) => {
  res.write('This is the list of our students\n');
  await countStudents(process.argv[2])
    .then((data = > {
      const fields = Object.keys(data);
      const }))


  try {
    const data = await countStudents(process.argv[2]);
    res.send(`${title}${data.join('\n')}`);
  } catch (error) {
    res.send(`${title}${error.message}`);
  }
});
app.listen(1245);
module.exports = app;
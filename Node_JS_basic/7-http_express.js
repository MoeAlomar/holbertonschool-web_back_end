const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const DB_PATH = process.argv[2];

app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});


app.get('/students', (req, res) => {
    res.set('Content-Type', 'text/plain');
    countStudents(DB_PATH)
        .then((data) => {
            res.send(`This is the list of our students\n${data}`);
        })
        .catch((err) => {
            res.end(`This is the list of our students\n${err.message}`);
        });
});

app.listen(1245);

module.exports = app;

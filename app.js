const express = require('express');
const mongoose = require('mongoose');
const app = express();
const port = 3000;

//MongoDB
mongoose.connect('mongodb://localhost:27017/formdata', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
    console.log('Connected to MongoDB');
});

const FormData = mongoose.model('FormData', {
    name: String,
    email: String
});

// Middleware
app.use(express.urlencoded({ extended: true }));

//EJS
app.set('view engine', 'ejs');

app.use(express.static('public'));

app.get('/', (req, res) => {
    res.render('index');
});

app.post('/', async (req, res) => {
    const formData = new FormData({
        name: req.body.name,
        email: req.body.email
    });

    try {
        await formData.save();
        console.log('Form data saved:', formData);
        res.redirect('/');
    } catch (err) {
        console.error(err);
        res.status(500).send('Internal Server Error');
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

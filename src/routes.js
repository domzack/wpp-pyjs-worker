const express = require('express');
const fs = require('fs');
const path = require('path');

const router = express.Router();

router.get('/', (req, res) => {
    const tokensDir = path.join(__dirname, '..', 'tokens');
    let sessionNames = [];
    try {
        sessionNames = fs.readdirSync(tokensDir, { withFileTypes: true })
            .filter(dirent => dirent.isDirectory())
            .map(dirent => dirent.name);
    } catch (err) {
        sessionNames = [];
    }
    res.render('index', { sessionNames });
});

module.exports = router;
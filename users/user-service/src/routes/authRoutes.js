const express = require('express');
const router = express.Router();
const { login, register, verifyToken } = require('../controllers/authController');

// Public Routes
router.post('/login', login);
router.post('/register', register);

// Protected Routes (contoh untuk menguji token JWT)
router.get('/protected-route', verifyToken, (req, res) => {
    res.json({ message: 'This is a protected route.', userId: req.userId });
});

module.exports = router;

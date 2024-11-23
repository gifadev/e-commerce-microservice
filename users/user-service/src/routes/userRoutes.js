const express = require('express');
const router = express.Router();
const UserController = require('../controllers/userController');
const { verifyToken } = require('../controllers/authController');

// CRUD Routes for Users
router.post('/', UserController.createUser);
router.get('/', verifyToken, UserController.getAllUsers);
router.get('/:id', verifyToken, UserController.getUserById);
router.put('/:id', verifyToken, UserController.updateUser);
router.delete('/:id', verifyToken, UserController.deleteUser);

router.get('/protected-route', verifyToken, (req, res) => {
    res.json({ message: 'This is a protected route.' });
});

module.exports = router;
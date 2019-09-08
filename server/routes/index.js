const usersController = require('../controllers').users;

module.exports = (app) => {
    app.get('/api', (req, res) => res.status(200).send({
        message: 'Welcome to the OpenRank API!',
    }));

    app.post('/api/users', usersController.create);
    app.get('/api/users', usersController.list);
};

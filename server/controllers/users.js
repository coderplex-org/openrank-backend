const User = require('../models').User;

module.exports = {
    create(req, res) {
        return User
            .create({
                username: req.body.email,
                email: req.body.email,
                name: req.body.name,
                password: req.body.password,
            })
            .then(user => res.status(201).send(user))
            .catch(error => res.status(400).send(error));
    },
    list(req, res) {
        return User
            .findAll()
            .then(users => res.status(200).send(users))
            .catch(error => res.status(400).send(error));
    }
};

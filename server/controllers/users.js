const jwt = require('jsonwebtoken');

const jwtOptions = require('../../app').jwtOptions;
const User = require('../models').User;

module.exports = {
    create(req, res) {
        const { email, name, password } = req.body;
        return User
            .create({
                username: email,
                email,
                name,
                password,
            })
            .then(user => res.status(201).json({ data: user }))
            .catch(error => res.status(400).json({ data: error }));
    },
    list(req, res) {
        return User
            .findAll()
            .then(users => res.status(200).json({ data: users }))
            .catch(error => res.status(400).json({ data: error }));
    },
    get(req, res) {
        const { id } = req.params;
        return User
            .findByPk(id)
            .then(user => res.status(200).json({ data: user }))
            .catch(error => res.status(400).json({ data: error }));
    },
    login(req, res) {
        const { email, password } = req.body;
        return User
            .findOne({ where: { email } })
            .then(user => {
                if (user.password === password) {
                    const payload = {id: user.id};
                    const token = jwt.sign(payload, jwtOptions.secretOrKey);
                    return res.json({ message: "ok", data: { token } });
                } else {
                    return res.status(401).json({ message: "Passwords did not match" });
                }
            })
            .catch(error => res.status(400).json({ data: error, message: 'No such user found' }));
    }
};

const express = require('express');
const logger = require('morgan');
const bodyParser = require('body-parser');

const jwt = require('jsonwebtoken');
const passport = require('passport');
const passportJWT = require('passport-jwt');

const User = require('./server/models').User;

const ExtractJwt = passportJWT.ExtractJwt;
const JwtStrategy = passportJWT.Strategy;

let jwtOptions = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: 'jwt-secret',
    passReqToCallback: true,
};
exports.jwtOptions = jwtOptions;

const strategy = new JwtStrategy(jwtOptions, function(req, jwt_payload, done) {
    return User
        .findOne({ where: { id: jwt_payload.id } })
        .then(user => {
            req.currentUser = user;
            done(null, user)
        })
        .catch(error => done(error, false));
});

passport.use(strategy);

// Set up the express app
const app = express();

// Log requests to the console.
app.use(logger('dev'));

// Parse incoming requests data (https://github.com/expressjs/body-parser)
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Require our routes into the application.
require('./server/routes')(app);
// Setup a default catch-all route that sends back a welcome message in JSON format.
app.get('*', (req, res) => res.status(200).send({
    message: 'Welcome to the beginning of nothingness.',
}));

module.exports = app;

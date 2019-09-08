const jwt = require('jsonwebtoken');
const passport = require('passport');
const passportJWT = require('passport-jwt');

const jwtConfig = require('./jwtConfig').jwtConfig;
const User = require('../models').User;

const ExtractJwt = passportJWT.ExtractJwt;
const JwtStrategy = passportJWT.Strategy;

const jwtOptions = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: jwtConfig.secret,
    passReqToCallback: true,
};

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

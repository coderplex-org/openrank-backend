const jwt = require('jsonwebtoken');
const passport = require('passport');
const passportJWT = require('passport-jwt');

const User = require('../models').User;
const jwtConfig = require('../config/jwtConfig').jwtConfig;

const ExtractJwt = passportJWT.ExtractJwt;
const JwtStrategy = passportJWT.Strategy;

let jwtOptions = {
    jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
    secretOrKey: jwtConfig.secret,
    passReqToCallback: true,
};

const strategy = new JwtStrategy(jwtOptions, function(jwt_payload, done) {
    return User
        .findOne({ where: { id: jwt_payload.id } })
        .then(user => done(null, user))
        .catch(error => done(error, false));
});

passport.use('jwt', strategy);

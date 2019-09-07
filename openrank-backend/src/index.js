import express from 'express';
import cors from 'cors';
import routes from './routes/index';
import * as jwt from "jsonwebtoken";
import * as config from "./config";
import {User} from './sequelize';

console.log('Starting OpenRank API Server');

const app = express();

var allowedOrigins = config.ALLOWED_ORIGINS;
app.use(cors({
    origin: function (origin, callback) {
        // allow requests with no origin
        // (like mobile apps or curl requests)
        if (!origin) return callback(null, true)
        if (allowedOrigins.indexOf(origin) === -1) {
            var msg = 'The CORS policy for this site does not allow access from the specified Origin.'
            return callback(new Error(msg), false)
        }
        return callback(null, true)
    }
 }))

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

app.use((req, res, next) => {
    try {
        const token = req.headers.authorization;
        if (token != null && token != undefined) {
            jwt.verify(token, config.tokenKey, async (err, payload) => {
                if (payload) {
                    // TODO: Change code based on User Model
                    // req.user = await User.getUserByUsername(payload.username)
                }
                next()
            })
        } else {
            next()
        }
    } catch (error) {
        next()
    }
 })


//Add handlers for routes here
app.get('/', routes);

app.listen(8000, () =>
console.log('Example app listening on port 8000!'),
)

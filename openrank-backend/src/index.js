import express from 'express';
import cors from 'cors';
import routes from './routes'

console.log('Starting OpenRank API Server');

const app = express();
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

//Add handlers for routes here

app.get('/', routes.home);

sequelize.sync().then(() => {
    app.listen(8000, () =>
        console.log('Example app listening on port 8000!'),
    )
});
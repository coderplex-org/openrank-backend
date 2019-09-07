import Sequelize from 'sequelize'
import env from './config';
import UserModel from './models/user'

const sequelize = new Sequelize(env.DATABASE.DB_NAME, env.DATABASE.DB_USER, env.DATABASE.DB_PASSWORD, {
  host: env.DATABASE.HOST,
  dialect: env.DATABASE.DIALECT,
  pool: {
    max: 10,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
})

sequelize
  .authenticate()
  .then(function(err) {
    console.log('Connection has been established successfully.');
  })
  .catch(function (err) {
    console.log('Unable to connect to the database:', err);
    return err;
  });

const User = UserModel(sequelize, Sequelize)

// force : true means the db will be dropped if it already exists
sequelize.sync({ force: true })
  .then(() => {
    console.log(`Database & tables created!`)
  })

module.exports = {
  User,
}
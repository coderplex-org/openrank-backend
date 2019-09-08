'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('Users', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      username: {
        type: Sequelize.STRING,
        unique: true,
        notEmpty: true,
        allowNull: false,
      },
      name: {
        type: Sequelize.STRING,
        notEmpty: true,
        allowNull: false,
      },
      email: {
        type: Sequelize.STRING,
        unique: true,
        notEmpty: true,
        allowNull: false,
      },
      password: {
        type: Sequelize.STRING,
        notEmpty: true,
        allowNull: false,
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: (queryInterface, Sequelize) => {
    return queryInterface.dropTable('Users');
  }
};

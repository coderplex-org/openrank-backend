module.exports = {
    TOKEN : process.env.TOKEN || 'openranksecrettoken',
    ALLOWED_ORIGINS: ['http://localhost:3000'],
    PORT : process.env.PORT || 8000,
    DATABASE :{
        DB_NAME: process.env.DATABASE || 'openrank_db',
        DB_USER : process.env.DATABASE_USER || 'postgres',
        DB_PASSWORD : process.env.PASSWORD || 'local1234',
        HOST: process.env.HOST || 'localhost',
        DIALECT: process.env.DIALECT || 'postgres',
    }
}
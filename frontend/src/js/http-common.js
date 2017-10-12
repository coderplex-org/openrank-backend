import axios from 'axios';

export const HTTP = axios.create({
  baseURL: process.env.API_SERVER_URL,
  headers: {
    'Access-Control-Allow-Origin': '*',
    Authorization: 'Bearer {token}',
    'Access-Control-Allow-Methods': 'GET, POST, PUT'
  }
});

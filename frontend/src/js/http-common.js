import axios from 'axios';

export const HTTP = axios.create({
  baseURL: process.env.API_SERVER_URL,
  headers: {

  }
});

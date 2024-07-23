import axios, { AxiosError } from 'axios';
import { getCacheStorage, getRequestHeaders, setCacheStorage } from 'utils/cacheStorage';

const instance = axios.create({
  baseURL: '/api',
  timeout: 5000,
});

instance.interceptors.request.use(
  async config => {
    const headers = await getRequestHeaders(config);
    config.headers = headers;

    console.info('calling api');
    return config;
  },
  error => {
    return Promise.reject(error.response);
  }
);
instance.interceptors.response.use(
  async response => {
    await setCacheStorage(response);
    return response;
  },
  async error => {
    if (error instanceof AxiosError) {
      if (error.response?.status === 304) {
        const cached = await getCacheStorage(error);
        return cached;
      }
    }
    return Promise.reject(error.response);
  }
);

export default instance;

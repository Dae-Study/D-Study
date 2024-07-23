import { AxiosRequestConfig, AxiosResponse, AxiosError } from 'axios';

export const getRequestHeaders = async (config: AxiosRequestConfig) => {
  const queryStr = new URLSearchParams(config.params).toString();
  const cacheStorage = await caches.open(config.url ? config.url : '');

  const cachedResponse = await cacheStorage.match(queryStr);
  const cached = await cachedResponse?.json();

  return {
    'If-None-Match': cached ? `${cached.etag}` : '',
  };
};

export const setCacheStorage = async (response: AxiosResponse) => {
  const customData = {
    etag: response.headers.etag,
    data: response.data,
  };

  const queryStr = new URLSearchParams(response.config.params).toString();
  const cacheStorage = await caches.open(response.config.url ? response.config.url : '');
  cacheStorage.put(queryStr, new Response(JSON.stringify(customData)));
};

export const getCacheStorage = async (error: AxiosError) => {
  if (error.config) {
    const queryStr = new URLSearchParams(error.config.params).toString();
    const cacheStorage = await caches.open(error.config.url ? error.config.url : '');
    const cachedResponse = await cacheStorage.match(queryStr);
    const cached = await cachedResponse?.json();
    return cached;
  }

  return { data: [] };
};

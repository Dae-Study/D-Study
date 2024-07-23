import instance from './axiosInstance';
import { ISicks } from '@types';
import axios, { AxiosError } from 'axios';

const URL_SICK = 'sick';

export const getSick = async (param: string): Promise<ISicks[]> => {
  if (param === '') return [];

  if ('caches' in window) {
    const config = {
      params: {
        sickNm_like: param,
      },
    };
    try {
      const response = await instance.get(`/${URL_SICK}`, config);
      return response.data;
    } catch (error) {
      const err = error as AxiosError;
      if (axios.isAxiosError(err)) {
        console.error(err);
      }
    }
  }

  return [];
};

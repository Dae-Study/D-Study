import { ISicks } from '@types';

export const wrapPromise = (promise: Promise<ISicks[]>) => {
  let status = 'pending';
  let result: ISicks[] | [];
  let suspend = promise.then(
    res => {
      status = 'success';
      result = res;
    },
    err => {
      status = 'error';
      result = err;
    }
  );
  return {
    read() {
      if (status === 'pending') {
        throw suspend;
      } else if (status === 'error') {
        throw result;
      } else {
        return result;
      }
    },
  };
};

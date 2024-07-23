import { IResultItems } from '@types';
import { getSick } from 'apis/ClinicalService';
import { wrapPromise } from 'utils/wrapPromise';
import { useEffect, useMemo, useState } from 'react';
import { useAppDispatch } from 'redux/hooks';

const useGetSickItem = (searchWord: string) => {
  const dispatch = useAppDispatch();
  const initItems = useMemo(() => {
    return {
      read: () => [],
    };
  }, []);
  const [items, setItems] = useState<IResultItems>(initItems);

  useEffect(() => {
    if (searchWord === null || searchWord.trim() === '') {
      setItems(initItems);
      return;
    }

    const getSickName = () => {
      const searchResult = getSick(searchWord);
      setItems(wrapPromise(searchResult));
    };
    const delay = setTimeout(() => getSickName(), 300);

    return () => clearTimeout(delay);
  }, [searchWord, dispatch, initItems]);

  return items;
};

export default useGetSickItem;

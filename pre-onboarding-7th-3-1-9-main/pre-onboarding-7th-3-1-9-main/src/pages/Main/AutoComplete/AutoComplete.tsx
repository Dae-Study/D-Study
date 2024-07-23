import { useEffect } from 'react';
import useGetSickItem from 'hooks/useGetSickItem';
import { useAppDispatch, useAppSelector } from 'redux/hooks';
import { setItemsLength } from 'redux/reducer/searchSlice';
import AutoCompleteItem from 'components/blocks/AutoCompleteItem';
import EmptyResult from 'components/blocks/EmptyResult';
import Recommand from 'components/blocks/Recommand';

const AutoComplete = () => {
  const { searchWord, selectIndex } = useAppSelector(({ search }) => search);

  const resource = useGetSickItem(searchWord);
  const data = resource.read();

  const dispatch = useAppDispatch();
  useEffect(() => {
    dispatch(setItemsLength(data.length));
  }, [dispatch, data]);

  return (
    <>
      {data.length > 0 && searchWord !== '' && <Recommand searchWord={searchWord} />}
      <div>
        {data.map(({ sickNm }, index) => {
          const textArray = sickNm.split(searchWord);
          return (
            <AutoCompleteItem
              key={index}
              index={index}
              searchWord={searchWord}
              selectIndex={selectIndex}
              textArray={textArray}
            />
          );
        })}
      </div>
      {data.length === 0 && <EmptyResult />}
    </>
  );
};

export default AutoComplete;

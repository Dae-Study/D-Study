import React from 'react';
import SearchBarUI from './SearchBar';
import { useAppDispatch, useAppSelector } from 'redux/hooks';
import { setSearchWord, setIsOpen, setSelectIndex } from 'redux/reducer/searchSlice';

const SearchBarIndex = () => {
  const dispatch = useAppDispatch();
  const { itemsLength, selectIndex } = useAppSelector(({ search }) => search);

  const onSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    dispatch(setSearchWord(e.target.value));

    if (e.target.value === '') {
      dispatch(setSelectIndex(-1));
    }
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (!e.nativeEvent.isComposing) {
      if (e.key === 'ArrowDown' && itemsLength - 1 > selectIndex) {
        dispatch(setSelectIndex(selectIndex + 1));
      }
      if (e.key === 'ArrowUp' && selectIndex >= 0) {
        dispatch(setSelectIndex(selectIndex - 1));
      }
    }
  };

  const onFocusInput = () => {
    dispatch(setIsOpen(true));
  };

  const onBlur = () => {
    dispatch(setIsOpen(false));
  };
  return (
    <>
      <SearchBarUI
        onChange={onSearchChange}
        onFocus={onFocusInput}
        onBlur={onBlur}
        onKeyDown={onKeyDown}
      />
    </>
  );
};

export default SearchBarIndex;

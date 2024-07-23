import React, { Suspense } from 'react';
import { useAppSelector } from 'redux/hooks';
import { DropDownBox } from './styles';
import LoadingText from 'components/blocks/LoadingText';
import AutoComplete from './AutoComplete';

const AutoCompleteIndex = () => {
  const isOpen = useAppSelector(({ search }) => search.isOpen);

  return (
    <DropDownBox className={isOpen ? 'active' : ''}>
      <Suspense fallback={<LoadingText />}>
        <AutoComplete />
      </Suspense>
    </DropDownBox>
  );
};

export default AutoCompleteIndex;

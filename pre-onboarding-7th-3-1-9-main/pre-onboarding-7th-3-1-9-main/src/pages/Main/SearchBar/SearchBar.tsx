import React from 'react';
import { ReactComponent as Magnifying } from 'assets/Magnifying.svg';
import { useAppSelector } from 'redux/hooks';
import { StyledBorder, StyledInput, StyledSearchSection } from './styles';

const SearchBar = ({
  onChange,
  onFocus,
  onBlur,
  onKeyDown,
}: React.InputHTMLAttributes<HTMLInputElement>) => {
  const { searchWord } = useAppSelector(({ search }) => search);

  return (
    <StyledSearchSection>
      <span className="search_icon">
        <Magnifying />
      </span>
      <StyledInput
        type="search"
        value={searchWord}
        onChange={onChange}
        onFocus={onFocus}
        onBlur={onBlur}
        onKeyDown={onKeyDown}
        placeholder="질환명을 입력해주세요."
      />
      <StyledBorder>
        <span>검색</span>
      </StyledBorder>
    </StyledSearchSection>
  );
};

export default SearchBar;

import React from 'react';
import AutoComplete from './AutoComplete';
import SearchBar from './SearchBar';
import { StyledHeader, StyledMain, StyledSearchDiv, StyledTitle } from './styles';

const MainPage = () => {
  return (
    <>
      <StyledHeader />
      <StyledMain>
        <StyledTitle>
          <h2>
            국내 모든 임상시험 검색하고
            <br />
            온라인으로 참여하기
          </h2>
        </StyledTitle>
        <StyledSearchDiv>
          <SearchBar />
          <AutoComplete />
        </StyledSearchDiv>
      </StyledMain>
    </>
  );
};

export default MainPage;

import styled from 'styled-components';

export const StyledHeader = styled.header`
  width: 100%;
  height: 56px;
`;

export const StyledMain = styled.main`
  display: flex;

  flex-direction: column;
  justify-content: center;
  width: 100%;
  height: 462px;
  background-color: #cae9ff;

  padding: 80px 0 160px;
`;

export const StyledTitle = styled.div`
  margin: 0 auto;
  margin-bottom: 40px;

  h2 {
    font-size: 2.125rem;
    font-weight: bold;
    line-height: 3rem;
    text-align: center;
  }
`;

export const StyledSearchDiv = styled.div`
  width: 490px;
  margin: 0 auto;

  position: relative;
`;

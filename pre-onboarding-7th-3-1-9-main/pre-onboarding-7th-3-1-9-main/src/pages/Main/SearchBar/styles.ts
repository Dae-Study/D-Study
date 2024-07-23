import styled from 'styled-components';

export const StyledSearchSection = styled.div`
  position: relative;

  span.search_icon {
    position: absolute;
    width: 16px;
    top: 27px;
    left: 25px;

    z-index: 1;
  }
`;

export const StyledBorder = styled.div`
  position: absolute;
  width: 15%;
  height: 100%;
  top: 0;
  right: 0;
  border-top-right-radius: 42px;
  border-bottom-right-radius: 42px;
  background-color: #4a78dc;
  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;

  span {
    padding-right: 10px;
    font-weight: bold;
    font-size: 1.2em;
    color: #fff;
  }
`;

export const StyledInput = styled.input`
  width: 100%;

  border-radius: 42px;
  border: 2px solid;
  border-color: #ffffff;
  background-color: #ffffff;
  -webkit-flex-direction: row;
  -ms-flex-direction: row;
  flex-direction: row;
  -webkit-align-items: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  font-size: 1rem;
  font-weight: 400;
  letter-spacing: -0.018em;
  line-height: 1.6;
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
  width: 100%;
  position: relative;

  padding: 20px 80px 20px 48px;
`;

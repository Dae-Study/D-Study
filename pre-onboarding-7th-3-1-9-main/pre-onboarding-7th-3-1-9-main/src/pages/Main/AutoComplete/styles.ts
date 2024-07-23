import styled from 'styled-components';

export const DropDownBox = styled.ul`
  display: none;

  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  border-bottom-left-radius: 20px;
  background-color: rgb(255, 255, 255);

  width: 100%;
  top: 100%;
  left: 0px;
  margin-top: 8px;
  padding: 20px 0;
  box-shadow: rgba(30, 32, 37, 0.1) 0px 2px 10px;
  position: absolute;

  &.active {
    display: block;
  }

  > div {
    display: flex;
    flex-direction: column;
    max-height: 400px;
    overflow: auto;
  }

  p {
    padding-left: 16px;
    font-size: 12px;
    line-height: 12px;
    color: #6c737b;

    margin: 8px 0;
  }
`;

export const DropDownItem = styled.li`
  position: relative;
  padding: 0 16px 0 42px;
  height: 42px;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  flex: 0 0 auto;
  &.over {
    background-color: #e2e2e2;
  }
  span.search_icon {
    position: absolute;
    width: 16px;
    top: 14px;
    left: 18px;

    z-index: 1;
  }
  span.search_text {
    line-height: 42px;

    span.font_bold {
      font-weight: bold;
    }
  }
`;

import { DropDownItem } from 'pages/Main/AutoComplete/styles';

const EmptyResult = () => {
  return (
    <DropDownItem>
      <span className="search_text">검색어가 없습니다</span>
    </DropDownItem>
  );
};

export default EmptyResult;

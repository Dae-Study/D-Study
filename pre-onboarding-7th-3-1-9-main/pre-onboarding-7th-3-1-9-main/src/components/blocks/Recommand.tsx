import { ReactComponent as Magnifying } from 'assets/Magnifying.svg';
import { DropDownItem } from 'pages/Main/AutoComplete/styles';

const Recommand = ({ searchWord }: { searchWord: string }) => {
  return (
    <>
      <DropDownItem>
        <span className="search_icon">
          <Magnifying />
        </span>
        <span className="search_text">
          <span className="font_bold">{searchWord}</span>
        </span>
      </DropDownItem>
      <p>추천 검색어</p>
    </>
  );
};

export default Recommand;

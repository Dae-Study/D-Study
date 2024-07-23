import { ReactComponent as Magnifying } from 'assets/Magnifying.svg';
import { DropDownItem } from 'pages/Main/AutoComplete/styles';

const AutoCompleteItem = ({
  index,
  searchWord,
  selectIndex,
  textArray,
}: {
  index: number;
  searchWord: string;
  selectIndex: number;
  textArray: string[];
}) => {
  return (
    <DropDownItem className={selectIndex === index ? 'over' : ''}>
      <span className="search_icon">
        <Magnifying />
      </span>
      {textArray.map((item, i) => (
        <span key={i} className="search_text">
          {item}
          {i !== textArray.length - 1 && <span className="font_bold">{searchWord}</span>}
        </span>
      ))}
    </DropDownItem>
  );
};

export default AutoCompleteItem;

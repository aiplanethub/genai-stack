import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";

import { neutral, primary, white } from "../../../common/config/colors";

const StyledListItem: React.FC<{
  isListItemActive: boolean;
  listItemId: number;
  listItemLabel: string;
  open: boolean;
  listItemIcon?: React.ReactChild;
  onChangeActiveListItem: (listItemId: number) => void;
}> = ({
  isListItemActive,
  listItemId,
  listItemLabel,
  open,
  listItemIcon,
  onChangeActiveListItem,
}) => {
  return (
    <ListItem
      onClick={() => onChangeActiveListItem(listItemId)}
      sx={{
        maxWidth: !!listItemIcon ? 250 : 296,
        borderRadius: "0 30px 30px 0",
        cursor: "pointer",
        py: 2.75,
        pl: !!listItemIcon
          ? isListItemActive
            ? 4.25
            : 5
          : isListItemActive
          ? 10.25
          : 11,
        "&:hover": {
          backgroundColor: white[800],
        },
        ...(isListItemActive &&
          open && {
            borderLeftWidth: "3px",
            borderLeftStyle: "solid",
            borderColor: primary[900],
            backgroundColor: white[800],
          }),
      }}
    >
      {!!listItemIcon && (
        <ListItemIcon sx={{ minWidth: 0, mr: 2.5 }}>
          {listItemIcon}
        </ListItemIcon>
      )}
      <ListItemText
        sx={{
          opacity: open ? 1 : 0,
          "& .MuiTypography-root": {
            fontSize: 14,
            fontWeight: 600,
            color: isListItemActive ? primary[900] : neutral[400],
          },
        }}
      >
        {listItemLabel}
      </ListItemText>
    </ListItem>
  );
};

export default StyledListItem;

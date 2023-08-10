import Image from "next/image";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText, { ListItemTextProps } from "@mui/material/ListItemText";

import { neutral } from "../../../common/config/colors";

const SingleListItem: React.FC<{
  labelProps: ListItemTextProps;
  icon: string;
  open: boolean;
  children?: React.ReactNode;
}> = ({ labelProps, icon, open, children }) => {
  return (
    <ListItem sx={{ p: 2 }}>
      <ListItemIcon
        sx={{
          minWidth: 0,
          mr: 3,
        }}
      >
        <Image src={icon} width={25} height={25} alt={icon} />
      </ListItemIcon>
      <ListItemText
        {...labelProps}
        sx={{
          opacity: open ? 1 : 0,
          "& .MuiTypography-root": {
            fontSize: 16,
            fontWeight: 500,
            color: neutral[900],
          },
          ...(labelProps?.sx || {}),
        }}
      />
      {children}
    </ListItem>
  );
};

export default SingleListItem;

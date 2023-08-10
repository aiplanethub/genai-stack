import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import DocumentScannerOutlinedIcon from "@mui/icons-material/DocumentScannerOutlined";
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";

// import ProfileListItem from "../../../ds/common/components/layout/profile/ProfileListItem";
import { neutral, white } from "../../common/config/colors";

const BottomMenu: React.FC<{ open: boolean }> = ({ open }) => {
  const menuItems = [
    {
      name: "Documentation",
      icon: (
        <DocumentScannerOutlinedIcon
          fontSize="small"
          sx={{ color: neutral[500] }}
        />
      ),
    },
    {
      name: "Feedback",
      icon: (
        <HelpOutlineOutlinedIcon
          fontSize="small"
          sx={{ color: neutral[500] }}
        />
      ),
    },
  ];

  return (
    <Box>
      <List
        disablePadding
        sx={{
          border: "1px solid #E3E8EF",
          borderLeft: "none",
          borderRight: "none",
          "& .MuiListItem-divider": {
            borderColor: "#E3E8EF",
          },
        }}
      >
        {menuItems.map((menuItem, id) => (
          <ListItem
            key={id}
            sx={{
              px: 2,
              py: 2.75,
              cursor: "pointer",
              "&:hover": { backgroundColor: white[800] },
            }}
            divider={id == 0}
          >
            <ListItemIcon sx={{ minWidth: 0, mr: 3 }}>
              {menuItem.icon}
            </ListItemIcon>
            <ListItemText
              sx={{
                opacity: open ? 1 : 0,
                "& .MuiTypography-root": {
                  fontWeight: 500,
                },
              }}
            >
              {menuItem.name}
            </ListItemText>
          </ListItem>
        ))}
      </List>
      {/* <List
        disablePadding
        sx={{
          "& .MuiListItem-root": {
            my: 0,
            "& .MuiBox-root": {
              width: "100%",
              borderRadius: 0,
              borderTop: "none",
              borderLeft: "none",
              borderRight: "none",
              borderColor: "#E3E8EF",
              "& .MuiAvatar-root": {
                width: 25,
                height: 25,
                fontSize: 14,
                fontWeight: 700,
              },
              "& .MuiTypography-root": {
                opacity: open ? 1 : 0,
                px: 1,
              },
            },
          },
        }}
      >
        <ProfileListItem />
      </List> */}
    </Box>
  );
};

export default BottomMenu;

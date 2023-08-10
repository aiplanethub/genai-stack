"use client";

import { useState } from "react";
import Box from "@mui/material/Box";
import MuiDrawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import IconButton from "@mui/material/IconButton";
import AddCircleOutlineOutlinedIcon from "@mui/icons-material/AddCircleOutlineOutlined";
import { styled, Theme, CSSObject } from "@mui/material/styles";

import usePDFConverse from "../context/usePDFConverse";
import SingleListItem from "./common/SingleListItem";
import StyledListItem from "./common/StyledListItem";
import BottomMenu from "./BottomMenu";
import { AI_LOGO, CONVERSATION_ICON } from "../utils/constants";
import { neutral } from "../../common/config/colors";

const openedMixin = (theme: Theme): CSSObject => ({
  width: 313,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.enteringScreen,
  }),
  overflowX: "hidden",
});

const closedMixin = (theme: Theme): CSSObject => ({
  width: 44,
  transition: theme.transitions.create("width", {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  overflowX: "hidden",
});

const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  height: "100vh",
  whiteSpace: "nowrap",
  ...(open && {
    ...openedMixin(theme),
    "& .MuiDrawer-paper": openedMixin(theme),
  }),
  ...(!open && {
    ...closedMixin(theme),
    "& .MuiDrawer-paper": closedMixin(theme),
  }),
}));

const Sidebar = () => {
  const [open, setOpen] = useState(false);
  const {
    conversations,
    setConversations,
    selectedConversation,
    setSelectedConversation,
  } = usePDFConverse();

  const handleOpenDrawer = () => {
    setOpen(true);
  };

  const handleCloseDrawer = () => {
    setOpen(false);
  };

  const onConversationChange = (conversationItemId: number) => {
    setSelectedConversation(conversations[conversationItemId]);
  };

  const handleAddNewConversation = () => {
    const lastConversationIndex = conversations[conversations.length - 1].id;

    const totalConversationsWithDefaultName = conversations.reduce(
      (prev, curr) => {
        if (curr.name.startsWith("New Document")) {
          prev = prev + 1;
        }
        return prev;
      },
      0
    );

    setConversations([
      ...conversations,
      {
        id: lastConversationIndex + 1,
        name:
          totalConversationsWithDefaultName === 0
            ? "New Document"
            : `New Document (${totalConversationsWithDefaultName})`,
        file: [],
      },
    ]);
  };

  return (
    <Box maxWidth={44}>
      <Drawer
        variant="permanent"
        open={open}
        onMouseEnter={handleOpenDrawer}
        onMouseLeave={handleCloseDrawer}
      >
        <Box
          height="100%"
          display="flex"
          flexDirection="column"
          justifyContent="space-between"
        >
          <Box>
            {/* App Name Item */}
            <SingleListItem
              labelProps={{ children: "PDF Converse" }}
              icon={AI_LOGO}
              open={open}
            />
            {/* Conversation Title Item */}
            <SingleListItem
              labelProps={{
                children: "MY CONVERSATIONS",
                sx: {
                  "& .MuiTypography-root": {
                    fontSize: 14,
                    fontWeight: 600,
                    color: neutral[500],
                  },
                },
              }}
              icon={CONVERSATION_ICON}
              open={open}
            >
              <IconButton
                sx={{ opacity: open ? 1 : 0 }}
                onClick={handleAddNewConversation}
              >
                <AddCircleOutlineOutlinedIcon
                  fontSize="small"
                  sx={{ color: neutral[400] }}
                />
              </IconButton>
            </SingleListItem>
            {/* Conversations List */}
            <Box
              sx={{
                maxHeight: "calc(100vh - 208px)",
                overflowY: "scroll",
              }}
            >
              <List
                disablePadding
                sx={{ display: "flex", flexDirection: "column", rowGap: 1 }}
              >
                {conversations.map((conversation, id) => (
                  <StyledListItem
                    key={id}
                    isListItemActive={
                      selectedConversation.id === conversation.id
                    }
                    listItemId={id}
                    listItemLabel={conversation.name}
                    open={open}
                    onChangeActiveListItem={onConversationChange}
                  />
                ))}
              </List>
            </Box>
          </Box>
          <BottomMenu open={open} />
        </Box>
      </Drawer>
    </Box>
  );
};

export default Sidebar;

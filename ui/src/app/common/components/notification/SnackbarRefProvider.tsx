import React, { useRef } from "react";
import { SnackbarProvider } from "notistack";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";

const SnackbarRefProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const notistackRef = useRef<any>();
  const onDismiss = (key: any) => () => {
    notistackRef.current.closeSnackbar(key);
  };

  return (
    <SnackbarProvider
      maxSnack={3}
      ref={notistackRef}
      action={(key) => (
        <IconButton onClick={onDismiss(key)} size="small">
          <CloseIcon fontSize="medium" />
        </IconButton>
      )}
    >
      {children}
    </SnackbarProvider>
  );
};
SnackbarRefProvider.displayName = "SnackbarRefProvider";

export default SnackbarRefProvider;

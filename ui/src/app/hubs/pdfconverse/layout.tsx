import Box from "@mui/material/Box";

import PDFConverseProvider from "@/pdf-converse/context/PDFConverseProvider";
import Sidebar from "../../../pdf-converse/components/Sidebar";

export default function PDFConverseLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <Box display="flex">
      <PDFConverseProvider>
        <Sidebar />
      </PDFConverseProvider>
      {children}
    </Box>
  );
}

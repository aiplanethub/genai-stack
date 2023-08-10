import { useContext } from "react";

import PDFConverseContext from "./PDFConverseContext";
import { NSPDFConverse } from "../types";

const usePDFConverse = () => {
  const context = useContext(PDFConverseContext);
  if (context === undefined) {
    throw new Error(
      "usePDFConverse must be used within a PDFConverseContext.Provider."
    );
  }
  return context as NSPDFConverse.IPDFConverseContextProps;
};

export default usePDFConverse;

import { createContext } from "react";

import { NSPDFConverse } from "../types";

const PDFConverseContext =
  createContext<NSPDFConverse.IPDFConverseContextProps | null>(null);

PDFConverseContext.displayName = "PDFConverseContext";

export default PDFConverseContext;

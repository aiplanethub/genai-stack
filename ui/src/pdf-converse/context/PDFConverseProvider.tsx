"use client";

import { useState } from "react";

import PDFConverseContext from "./PDFConverseContext";
import { NSPDFConverse } from "../types";

const PDFConverseProvider: React.FC<{ children: React.ReactChild }> = ({
  children,
}) => {
  const [conversations, setConversations] = useState<
    NSPDFConverse.IConversationProps[]
  >([
    {
      id: 1,
      name: "AI PDF Getting Started",
      files: [
        { id: 1, name: "some file name" },
        { id: 2, name: "some file name" },
        { id: 3, name: "some file name" },
      ],
    },
    {
      id: 2,
      name: "AI PDF 2",
      files: [{ id: 1, name: "some file name" }],
    },
    {
      id: 3,
      name: "AI PDF 3",
      files: [],
    },
  ]);

  const [selectedConversation, setSelectedConversation] =
    useState<NSPDFConverse.IConversationProps>(conversations[0]);

  const [selectedFile, setSelectedFile] =
    useState<NSPDFConverse.IFileProps | null>(conversations[0].files[0]);

  return (
    <PDFConverseContext.Provider
      value={{
        conversations,
        setConversations,
        selectedConversation,
        setSelectedConversation,
        selectedFile,
        setSelectedFile,
      }}
    >
      {children}
    </PDFConverseContext.Provider>
  );
};

export default PDFConverseProvider;

export declare namespace NSPDFConverse {
  interface IFileProps {
    id: number;
    name: string;
  }

  interface IConversationProps {
    id: number;
    name: string;
    files: IFileProps[] | [];
  }

  interface IPDFConverseContextProps {
    conversations: IConversationProps[];
    setConversations: Dispatch<
      SetStateAction<NSPDFConverse.IConversationProps[]>
    >;
    selectedConversation: IConversationProps;
    setSelectedConversation: Dispatch<
      SetStateAction<NSPDFConverse.IConversationProps>
    >;
    selectedFile: IFileProps | null;
    setSelectedFile: Dispatch<SetStateAction<NSPDFConverse.IFileProps | null>>;
  }

  interface IConversationListItemProps {
    open: boolean;
    conversation: NSPDFConverse.IConversationProps;
    selectedConversationId: number;
    conversationItemId: number;
    onConversationChange: (conversationItemId: number) => void;
  }

  /* Chat Types */
  interface IChatConversationProps {
    role: "user" | "assistant";
    content: string;
  }
}

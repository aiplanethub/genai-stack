import Head from "next/head";

import ThemeRegistry from "../common/config/ThemeRegistry";
import "../../styles/globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" style={{ scrollBehavior: "smooth" }}>
      <Head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Inter:300,400,500,600,700&display=swap"
        />
      </Head>
      <body>
        <main>
          <ThemeRegistry>{children}</ThemeRegistry>
        </main>
      </body>
    </html>
  );
}

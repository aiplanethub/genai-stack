"use client";

import { useState } from "react";
import { useServerInsertedHTML } from "next/navigation";
import CssBaseline from "@mui/material/CssBaseline";
import createCache from "@emotion/cache";
import { ThemeProvider, CacheProvider } from "@emotion/react";

import theme from "./theme";

const ThemeRegistry: React.FC<{
  children: React.ReactNode;
}> = ({ children }) => {
  const [{ cache, flush }] = useState(() => {
    /**
     * prepend: true moves MUI styles to the top of the <head> so they're loaded first.
     * It allows developers to easily override MUI styles with other styling solutions, like CSS modules.
     * Currently, prepend does not work reliably with the App Router
     * Have to work around it by wrapping Emotion styles in a CSS @layer
     * __html: options.prepend ? @layer emotion {${styles}}` : styles; at line 55, and with a modification to the snippet above
     * https://mui.com/material-ui/guides/next-js-app-router/#css-injection-order
     **/
    const cache = createCache({ key: "mui", prepend: false });
    cache.compat = true;
    const prevInsert = cache.insert;
    let inserted: string[] = [];
    cache.insert = (...args) => {
      const serialized = args[1];
      if (cache.inserted[serialized.name] === undefined) {
        inserted.push(serialized.name);
      }
      return prevInsert(...args);
    };
    const flush = () => {
      const prevInserted = inserted;
      inserted = [];
      return prevInserted;
    };
    return { cache, flush };
  });

  useServerInsertedHTML(() => {
    const names = flush();
    if (names.length === 0) {
      return null;
    }
    let styles = "";
    for (const name of names) {
      styles += cache.inserted[name];
    }
    return (
      <style
        key={cache.key}
        data-emotion={`${cache.key} ${names.join(" ")}`}
        dangerouslySetInnerHTML={{
          __html: styles,
        }}
      />
    );
  });

  return (
    <CacheProvider value={cache}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        {children}
      </ThemeProvider>
    </CacheProvider>
  );
};

export default ThemeRegistry;

import { createTheme } from "@mui/material/styles";
import { primary, secondary, white } from "./colors";

let theme = createTheme({
  breakpoints: {
    values: {
      xs: 0,
      sm: 545,
      md: 768,
      lg: 992,
      xl: 1200,
    },
  },
  status: {
    danger: "#ea1717",
  },

  palette: {
    primary: {
      main: primary[900],
      contrastText: "#FFFFFF",
    },
    secondary: {
      main: "#344346",
      contrastText: "#FFFFFF",
    },
    neutral: {
      main: "#444444",
      contrastText: "#FFFFFF",
    },
    text: {
      primary: "#444444",
      secondary: "#666666",
    },
  },

  spacing: 4,

  typography: {
    htmlFontSize: 14,
    fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
    fontSize: 14,
    fontWeightLight: 300,
    fontWeightRegular: 400,
    fontWeightMedium: 500,
    fontWeightBold: 700,
    h1: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 700,
      fontSize: 48,
      lineHeight: 1.167,
      letterSpacing: "-0.01562em",
      color: "#000000",
    },
    h2: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 700,
      fontSize: 36,
      lineHeight: 1.2,
      letterSpacing: "-0.00833em",
      color: "#000000",
    },
    h3: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 600,
      fontSize: 32,
      lineHeight: 1.167,
      letterSpacing: "0em",
      color: "#000000",
    },
    h4: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 600,
      fontSize: 28,
      lineHeight: 1.235,
      letterSpacing: "0.00735em",
      color: "#000000",
    },
    h5: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 600,
      fontSize: 24,
      lineHeight: 1.334,
      letterSpacing: "0em",
      color: "#000000",
    },
    h6: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 500,
      fontSize: 16,
      lineHeight: 1.6,
      letterSpacing: "0.0075em",
      color: "#000000",
    },
    subtitle1: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 500,
      fontSize: 18,
      lineHeight: 1.75,
      letterSpacing: "0.00938em",
      color: "#444444",
    },
    subtitle2: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 400,
      fontSize: 16,
      lineHeight: 1.57,
      letterSpacing: "0.00714em",
      color: "#444444",
    },
    body1: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 400,
      fontSize: 14,
      lineHeight: 1.5,
      letterSpacing: "0.00938em",
      color: "#444444",
    },
    body2: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 400,
      fontSize: 12,
      lineHeight: 1.5,
      letterSpacing: "0.01071em",
      color: "#444444",
    },
    caption: {
      fontFamily: "'Inter', 'Helvetica', 'Arial', sans-serif",
      fontWeight: 400,
      fontSize: 12,
      lineHeight: 1.5,
      letterSpacing: "0.01071em",
      color: "#444444",
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: "none",
          minWidth: "100px",
        },
        contained: {
          borderRadius: "10px",
        },
        outlined: {
          borderRadius: "10px",
        },
        containedPrimary: {
          backgroundColor: primary[900],
          color: white[900],
          "&:hover": {
            backgroundColor: primary[800],
          },
        },
        outlinedPrimary: {
          borderRadius: "10px",
          border: `1px solid ${primary[900]}`,
          color: primary[900],
          "&:hover": {
            backgroundColor: primary[900],
            color: secondary[100],
            border: `1px solid ${primary[900]}`,
          },
        },
        textPrimary: {
          color: primary[900],
        },
      },
    },
    MuiFormHelperText: {
      styleOverrides: {
        root: {
          marginLeft: 0,
        },
      },
    },
  },
});

declare module "@mui/material/styles/createTheme" {
  export interface Theme {
    status: {
      danger: React.CSSProperties["color"];
    };
    platform: string;
  }
  interface ThemeOptions {
    status: {
      danger: React.CSSProperties["color"];
    };
  }
}
declare module "@mui/material/styles/createPalette" {
  interface Palette {
    neutral: PaletteOptions["primary"];
  }
  interface PaletteOptions {
    neutral: PaletteOptions["primary"];
  }
}

export default theme;

import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: "class",
  content: ["./app/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}", "./lib/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#080b12",
        panel: "#111827",
        line: "rgba(148, 163, 184, 0.22)",
        mint: "#2dd4bf",
        lime: "#a3e635",
        danger: "#fb7185",
        amber: "#f59e0b"
      },
      boxShadow: {
        terminal: "0 24px 80px rgba(2, 6, 23, 0.28)"
      }
    }
  },
  plugins: []
};

export default config;


/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px'
    },
    extend: {
      colors: {
        darkRed: "#8B0203",
        mainRed: "#EB1414",
        heroColor: "#FEEED2",
      },
    },
  },
  plugins: [],
}


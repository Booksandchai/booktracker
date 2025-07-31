
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#0f3d2e',
          light: '#3d8f6b',
          dark: '#041e13',
          accent: '#b8f3d1',
        },
        night: '#0a0a0f',
      },
      fontFamily: {
        whimsical: ['Pinyon Script', 'serif'],
        body: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
};

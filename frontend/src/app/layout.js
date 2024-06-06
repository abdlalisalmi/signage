import "./globals.css";

export const metadata = {
  title: "Signage",
  description: "A digital signage platform for the modern world.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

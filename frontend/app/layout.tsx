import "./globals.css";

export const metadata = {
  title: "Digital Twin Dashboard",
  description: "Consent-Based MSME Cash-Flow Digital Twin",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

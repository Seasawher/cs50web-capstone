import { Html, Head, Main, NextScript } from 'next/document';
import Navbar from '../components/navbar';

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body className="bg-slate-900 text-white">
        <Navbar />
        <div className="mx-auto max-w-5xl px-3 py-5">
          <Main />
          <NextScript />
        </div>
      </body>
    </Html>
  );
}

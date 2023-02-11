import Head from 'next/head';
import Image from 'next/image';
import { Inter } from '@next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function Home() {
  return (
    <>
      <Head>
        <title>Capstone</title>
      </Head>
      <h1 className="text-3xl font-bold text-rose-300 underline">Hello NextJS and TailwindCSS!!</h1>
    </>
  );
}

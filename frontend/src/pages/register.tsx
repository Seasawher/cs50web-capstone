import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <>
      <Head>
        <title>Register</title>
      </Head>
      <section className="mx-auto max-w-xl">
        <h1 className="mb-6 text-3xl font-bold">Register</h1>
        <div className="mb-3 rounded-lg bg-slate-800 py-6 px-8"></div>
        <div className="mb-3 rounded-lg bg-slate-800 py-6 px-8">
          Already have an account?{' '}
          <Link className="text-sky-200 hover:text-sky-400 hover:underline" href="./login">
            Log In here.
          </Link>
        </div>
      </section>
    </>
  );
}

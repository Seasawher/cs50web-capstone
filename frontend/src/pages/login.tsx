import React from 'react';
import Head from 'next/head';
import Link from 'next/link';
import Input from '../components/input';
import SubmitButton from '../components/submitButton';

export default function Home() {
  return (
    <>
      <Head>
        <title>Login</title>
      </Head>
      <section className="mx-auto max-w-xl">
        <h1 className="mb-6 text-3xl font-bold">Login</h1>
        <div className="mb-3 rounded-lg bg-slate-800 py-6 px-8">
          <form>
            <div className="mb-6">
              <label htmlFor="id_username" className="mb-3 block text-sm font-medium">
                Username
              </label>
              <Input id="id_username" name="username" type="text" placeholder="Username" />
            </div>
            <div className="mb-6">
              <label htmlFor="id_password" className="mb-3 block text-sm font-medium">
                Password
              </label>
              <Input id="id_password" name="password" type="password" placeholder="Password" />
            </div>
            <SubmitButton name="Login" />
          </form>
        </div>
        <div className="mb-3 rounded-lg bg-slate-800 py-6 px-8">
          Don't have an account?{' '}
          <Link className="text-sky-200 hover:text-sky-400 hover:underline" href="./register">
            Register here.
          </Link>
        </div>
      </section>
    </>
  );
}

import React from 'react';
import Head from 'next/head';
import Link from 'next/link';
import Input from '../components/input';
import SubmitButton from '../components/submitButton';

export default function Home() {
  return (
    <>
      <Head>
        <title>Register</title>
      </Head>
      <section className="mx-auto max-w-xl">
        <h1 className="mb-6 text-3xl font-bold">Register</h1>
        <div className="mb-3 rounded-lg bg-slate-800 py-6 px-8">
          <form>
            <div className="mb-6">
              <label htmlFor="id_username" className="mb-3 block text-sm font-medium">
                Username
              </label>
              <Input id="id_username" name="username" type="text" placeholder="Username" />
            </div>
            <div className="mb-6">
              <label htmlFor="id_email" className="mb-3 block text-sm font-medium">
                Email Address
              </label>
              <Input id="id_email" name="email" type="text" placeholder="Email Address" />
            </div>
            <div className="mb-6">
              <label htmlFor="id_password" className="mb-3 block text-sm font-medium">
                Password
              </label>
              <Input id="id_password" name="password" type="password" placeholder="Password" />
            </div>
            <div className="mb-6">
              <label htmlFor="id_confirm_password" className="mb-3 block text-sm font-medium">
                Confirm Password
              </label>
              <Input id="id_confirm_password" name="confirm_password" type="password" placeholder="Confirm Password" />
            </div>
            <SubmitButton name="Register" />
          </form>
        </div>
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

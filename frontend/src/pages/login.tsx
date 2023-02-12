import React from 'react';
import Head from 'next/head';
import Link from 'next/link';

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
              <input
                type="text"
                id="id_username"
                placeholder="username"
                className="w-full rounded-lg
                        bg-gray-600 px-3
                        py-1 placeholder-gray-400 focus:caret-blue-500 focus:outline focus:outline-2 focus:outline-blue-500"
              ></input>
            </div>
            <div className="mb-6">
              <label htmlFor="id_password" className="mb-3 block text-sm font-medium">
                Password
              </label>
              <input
                type="password"
                id="id_password"
                placeholder="password"
                className="w-full rounded-lg bg-gray-600 px-3 py-1 placeholder-gray-400 focus:caret-blue-500 focus:outline focus:outline-2 focus:outline-blue-500"
              ></input>
            </div>
            <button
              type="submit"
              className="my-3 rounded-lg bg-cyan-600 px-5 py-1.5 font-medium text-white hover:bg-cyan-700 focus:outline focus:outline-2 focus:outline-blue-500"
            >
              Login
            </button>
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

import React from 'react';
import Link from 'next/link';

export default function Navbar() {
  return (
    <>
      <nav className="bg-slate-800">
        <div className="top-0 left-0 flex flex-row p-4">
          <div className="basis-3/6">
            <Link className="text-xl font-semibold text-sky-300 hover:text-sky-500" href="/">
              Capstone
            </Link>
          </div>
          <div className="text-l basis-3/6 text-right">
            <span className="mx-3 hover:text-sky-400 hover:underline">
              <Link href="./register">Log Out</Link>
              <Link href="./login">Log In</Link>
            </span>
          </div>
        </div>
      </nav>
    </>
  );
}

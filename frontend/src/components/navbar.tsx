import React from "react";
import Link from 'next/link'

export default function Navbar() {
  return (
    <>
      <nav className='bg-slate-800'>
        <div className='flex flex-row top-0 left-0 p-4'>
          <div className='basis-3/6'>
            <Link className="text-xl font-semibold text-sky-300 hover:text-sky-500"
              href="/">
              Capstone
            </Link>
          </div>
          <div className="basis-3/6 text-right text-l">
            <span className="hover:underline hover:text-sky-400 mx-3">
              <Link href="./logout">Log Out</Link>
              <Link href="./login">Log In</Link>
            </span>
          </div>
        </div>
      </nav>
    </>
  )
}

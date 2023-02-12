import React from 'react';

export default function SubmitButton({ name }: {name: string}) {
  return (
    <>
      <button
        type="submit"
        className="my-3 rounded-lg bg-cyan-600 px-5 py-1.5 font-medium text-white hover:bg-cyan-700 focus:outline focus:outline-2 focus:outline-blue-500"
      >
        { name }
      </button>
    </>
  );
}

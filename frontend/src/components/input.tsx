import React from 'react';

export default function Input({ label, type }: {label: string, type: string}) {
  const input_id = `id_${label}`;
  return (
    <>
      <input
        type={type}
        id={input_id}
        placeholder={label}
        className="w-full rounded-lg bg-gray-600 px-3 py-1 placeholder-gray-400 focus:caret-blue-500 focus:outline focus:outline-2 focus:outline-blue-500"
      ></input>
    </>
  );
}

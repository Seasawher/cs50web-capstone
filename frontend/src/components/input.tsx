import React from 'react';

export default function Input({
  id,
  name,
  type,
  placeholder,
}: {
  id: string;
  name: string;
  type: string;
  placeholder: string;
}) {
  return (
    <>
      <input
        type={type}
        id={id}
        name={name}
        placeholder={placeholder}
        className="w-full rounded-lg bg-gray-600 px-3 py-1 placeholder-gray-400 focus:caret-blue-500 focus:outline focus:outline-2 focus:outline-blue-500"
      ></input>
    </>
  );
}

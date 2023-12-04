import React from 'react'
import Link from 'next/link'
import Google from './Icons/Google';
import { Facebook } from 'lucide-react';
import Microsoft from './Icons/Microsoft';
export const Links = () => {
  return (
    <div>
      <div className="flex flex-row  flex-wrap px-3 gap-5 py-4 ">
        <div className="">
          <Link href="#" className="text-textbg">
            Forgot your Password?{" "}
          </Link>
        </div>
        <div className=" text-textbg">
          <Link href="#">Create an account </Link>
        </div>
      </div>

      <div className="flex flex-col   px-10">
        <div className="py-3">
          <h1>Or continue with:</h1>
        </div>
        <div className="flex flex-row justify-center items-center space-x-10">
          <Link href="#" className="">
            <Google />
          </Link>
          <Link href="#" className="">
            <Facebook />
          </Link>
          <Link href="#" className="">
            <Microsoft />
          </Link>
        </div>
      </div>
    </div>
  );
}

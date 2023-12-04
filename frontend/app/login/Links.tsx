import React from 'react'
import Link from 'next/link'
import Google from './Icons/Google';
import { Facebook } from 'lucide-react';
import Microsoft from './Icons/Microsoft';
export const Links = () => {
  return (
    <div>
      <div className="flex flex-row place-content-between px-10 py-4 ">
        <div className="">
          <Link href="#">Forgot your Password? </Link>
        </div>
        <div className="">
          <Link href="#">Create an account </Link>
        </div>
      </div>

      <div className='flex flex-col px-10'>
        <div className='py-5'>
          <h1>Or continue with</h1>
        </div>
        <div className='flex flex-row content-evenly gap-10'>
              <div className="">
                 <Google />
              </div>
              <div className="">
                 <Facebook />
              </div>
              <div className="">
                 <Microsoft />
              </div>
        </div>
      </div>
    </div>
  );
}

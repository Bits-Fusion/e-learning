"use client"
import React from "react";
import { Link } from "@nextui-org/react";

export default function Links() {
  return (
    <div className="flex flex-row gap-3 px-6 ">
      <div className="flex gap-2">
        <Link href="#">Forgot Your Password ?</Link>
          </div>
          <br />
      <div className="px-10">
        <Link href="#" className="flex gap-10">
                 Create an account
        </Link>
      </div>
    </div>
  );
}

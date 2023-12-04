import React from "react";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function Inputs() {
  return (
    <div className="flex flex-col gap-4 px-10  ">
      <div>
        <h3>Login</h3>
        <Input type="email" placeholder="Email" className="rounded-full" />
      </div>
      <div className="">
        <h3>Password</h3>
        <Input
          type="password"
          placeholder="password"
          className="rounded-full"
        />
      </div>

      <div className="place-self-center ">
        <Button
          className="rounded-lg">
          Login
        </Button>
      </div>
    </div>
  );
}

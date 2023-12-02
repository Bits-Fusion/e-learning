import React from "react";
import { Textarea } from "@nextui-org/react";
import UserIcon from "./UserIcon";
import Links from "./Link";
const LoginInput = () => {
  return (
    <div className="flex flex-col box-border h-80 w-96 p-4 border-4 ">
      <div className="login flex flex-col">
        <div className="font-mono flex flex-col">
          <strong>Log in</strong>
          <h2>we are glad that you are here</h2>
        </div>
        <div className="txt-area box-border flex flex-col p-10 ">
          <div className="username">
            <Textarea
              isInvalid={false}
              variant="bordered"
              label="Username"
              placeholder="Enter your username"
              //   errorMessage="The description should be at least 255 characters long."
              className="max-w-xs h-4 "
            />
          </div>
          <br />
          <br />
          <div className="password">
            <Textarea
              isInvalid={false}
              variant="bordered"
              label="Password"
              placeholder="Enter your Password"
              //   errorMessage="The description should be at least 255 characters long."
              className="max-w-xs h-4 "
            />
          </div>
        </div>
        {/* forgot your password */}
      
      </div>
    </div>
  );
};

export default LoginInput;

import Link from "next/link";
import React from "react";
import GoogleIcon from "./GoogleIcon";
import MicrosoftIcon from "./MicrosoftIcon";
import FacebookIcon from "./FacebookIcon";

const OptionLinks = () => {
  return (
    <>
     <div className="text px-5"><p>Or continue with </p></div>
      <div className="flex flex-row gap-5 px-6">
        <div className="GoogleButton">
          <Link href="www.Google.com">
            <GoogleIcon />
          </Link>
        </div>
        <div className="FacebookIcon">
          <Link href="www.Facebook.com">
            <FacebookIcon />
          </Link>
        </div>
        <div className="MicrosoftButton">
          <Link href="www.Microsoft.com">
            <MicrosoftIcon />
          </Link>
        </div>
      </div>
    </>
  );
};

export default OptionLinks;

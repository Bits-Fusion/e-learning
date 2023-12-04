import React from "react";
import Text from "./Text";
import Inputs from "./Input";
import { Links } from "./Links";
import Image from "next/image";
import background from "../../public/background.jpg";
import kid from "../../public/kid.png";
import Help from './Help'

const Page = () => {
  return (
    <>
      <div className="absolute bottom-3 right-10">
        <Help />
      </div>
      <div className="flex items-center justify-center h-screen">
        <div className="absolute -z-10 w-full h-screen">
          <Image
            src={background}
            alt="background-image"
            layout="fill"
            objectFit="cover"
          />
        </div>
        <div className="flex flex-row md:w-8/12  bg-loginbg  rounded-3xl overflow-hidden">
          <div className="md:w-1/2 m-auto ">
            <Text />
            <Inputs />
            <Links />
          </div>

          <div className="py-10 px-3  hidden md:flex ">
            <Image src={kid} alt="" />
          </div>
        </div>
        {/* <div className="bottom-0 right-0">
          <Help />
        </div> */}
      </div>
    </>
  );
};

export default Page;

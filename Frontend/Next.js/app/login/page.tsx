import { Main } from "next/document";
import MainCard from "./components/LoginInput";
import LoginInput from "./components/LoginInput";
import Links from "./components/Link";
import LoginButton from "./components/Button";
import OptionLinks from "./components/OptionLinks";
export default function Cards() {
    return (
        <div className="m-10">
            <LoginInput />
            <br />
            <Links />
            <br />
            <LoginButton />
            <br />
            <OptionLinks />
        </div>
    );
}

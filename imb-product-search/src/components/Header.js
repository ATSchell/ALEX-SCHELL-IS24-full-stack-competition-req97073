import './Header.css';
import React from "react";
import logo from '../img/logo.png';

const HeaderBar = () => {
    return (
        <div className="Header-Bar">
            <img src={logo} className="logo" alt="IMB Logo" />
            <div className="Header-Contents">
                Product Search Tool
            </div>
        </div>
    );
};

export default HeaderBar;
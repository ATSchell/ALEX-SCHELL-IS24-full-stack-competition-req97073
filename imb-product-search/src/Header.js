import './Header.css';
import React from "react";
import logo from './logo.png';

const HeaderBar = () => {
    return (
        <div className="Header-Bar">
            <img src={logo} className="logo" />
            <div className="Header-Contents">
                Product Search Tool
            </div>
        </div>
    );
};

export default HeaderBar;
import React from "react";
import { LoadTableForDev } from "./DataTable";
import './SearchBar.css';


// Search bar for finding products by dev or scrum master
function SearchBar({tableRefresh}) {
    const [searchOptions, setSearchOptions] = React.useState({
        SearchText: "",
        DevOrScrum: ""
    });

    const handleChange = (event) => {
        setSearchOptions ( {
            ...searchOptions,
            [event.target.id]: event.target.value,
        });
    };
    
    // send off search details to relevant endpoint
    const SendSearch = async(event) => {
        if (searchOptions.DevOrScrum === "Developer") {
            await LoadTableForDev(tableRefresh, searchOptions.SearchText,"developed");
        } else {
            await LoadTableForDev(tableRefresh, searchOptions.SearchText,"scrummed");           
        }
    }

    return (
        <div className="Search-Bar">
            Field to Search:
            <select id="DevOrScrum" onChange={handleChange}>
                <option value="Scrum Master">Scrum Master</option>
                <option value="Developer">Developer</option>
            </select>
            <input type="text" placeholder="Search for products" className="Search-Input" onChange={handleChange} id="SearchText"/>
            <button onClick={()=>SendSearch()}>Search Products</button>
        </div>
    )
}

export default SearchBar;
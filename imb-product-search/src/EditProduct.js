import React, { Component } from "react";

function EditProduct() {

    return (
        <form>
        <label>
            Product Name
            <input placeholder="Product Name" id="ProductName" 
            required/>
        </label>
        <label>
            Scrum Master
            <input placeholder="Scrum Master" id="ScrumMasterName" 
            required/>
        </label>
        <label>
            Owner
            <input placeholder="Product Owner" id="ProductOwnerName" 
            required/>
        </label>
        <label>
            Developers
            <input placeholder="Developer Names" id="Developers" 
            required/>
        </label>
        <label>
            Start Date
            <input placeholder="Start Date" id="StartDate" 
            required/>
        </label>
        <label>
            Methodology
            <select id="Methodology">
                <option value="Agile">Agile</option>
                <option value="Waterfall">Waterfall</option>
      </select>
        </label>
        <button type="submit">Submit</button>
    </form>
    )

};


export default EditProduct;
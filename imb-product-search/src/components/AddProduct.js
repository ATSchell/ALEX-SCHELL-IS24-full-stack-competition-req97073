import './AddProduct.css';
import React from "react";
import { LoadTable } from "./DataTable";

// Form and logic for adding a product to the database via API request
function AddProduct({tableLoader, setVisablity}) {
    const [product, setProduct] = React.useState({
        ProductName: "",
        ScrumMasterName: "",
        ProductOwnerName: "",
        Developers: "",
        StartDate: "",
        Methodology: "Agile"
    });

    // update the data from the form as needed
    const handleChange = (event) => {
        setProduct ( {
            ...product,
            [event.target.id]: event.target.value,
        });
    };

    // generate an API POST request to add a new Product
    const handleAddProduct = async(event) => {
        event.preventDefault();
        console.log(typeof(tableLoader));
        // setup the POST request we'll send
        const postOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ProductName: product.ProductName, ScrumMasterName: product.ScrumMasterName, ProductOwnerName: product.ProductOwnerName,
                                Developers: product.Developers, StartDate: product.StartDate, Methodology: product.Methodology})
        };
        // send the POST Request
        await fetch("http://localhost:3000/api/product",postOptions).catch((error) => {console.log(error)});
        LoadTable(tableLoader);
        setVisablity(false);
        console.log("POST Done");
    };//handleAddProduct

    return (
        <form onSubmit={handleAddProduct}>
            <label>
                Product Name
                <input placeholder="Product Name" id="ProductName" 
                value={product.ProductName} onChange={handleChange} required/>
            </label>
            <label>
                Scrum Master
                <input placeholder="Scrum Master" id="ScrumMasterName" 
                value={product.ScrumMasterName} onChange={handleChange} required/>
            </label>
            <label>
                Owner
                <input placeholder="Product Owner" id="ProductOwnerName" 
                value={product.ProductOwnerName} onChange={handleChange} required/>
            </label>
            <label>
                Developers
                <input placeholder="Developer Names" id="Developers" 
                value={product.Developers} onChange={handleChange} required/>
            </label>
            <label>
                Start Date
                <input placeholder="Start Date" id="StartDate" 
                value={product.StartDate} onChange={handleChange} required/>
            </label>
            <label>
                Methodology
                <select value={product.Methodology} onChange={handleChange} id="Methodology">
                    <option value="Agile">Agile</option>
                    <option value="Waterfall">Waterfall</option>
                </select>
            </label>
            <button type="submit">Submit</button>
        </form>
    )
};//addproduct

export default AddProduct;

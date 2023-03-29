import React, { useState } from "react";
import editIcon from './edit_icon.png';
import deleteIcon from './delete_icon.png';
import confirmIcon from './check_icon.png';
import exitIcon from './exit_icon.png';

function TableElement({product, id}) {
    const [editVis, setEditVis] = useState(false);
    const [editProduct, setEditProduct] = React.useState({
        ProductID: product.ProductID,
        ProductName: product.ProductName,
        ScrumMasterName: product.ScrumMasterName,
        ProductOwnerName: product.ProductOwnerName,
        Developers: product.Developers,
        StartDate: product.StartDate,
        Methodology: product.Methodology
    });

    const handleChange = (event) => {
        setEditProduct ( {
            ...editProduct,
            [event.target.id]: event.target.value,
        });
    }


    //Function for deleting on click on relevant button 
    function DeleteItem({product}) {
        console.log("Deleting ID:"+product.ProductID);
        const deleteOptions = {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        };
        fetch('http://127.0.0.1:3000/api/product/'+product.ProductID,deleteOptions);
    };// DeleteItem

    //Function for editing on click on relevant button 
    function ToggleEdit({product}) {
        setEditVis(!editVis);
    };// EditItem

    function SubmitEdit({product}) {
        console.log("send to PUT command");
        console.log(editProduct.ProductName)
        const putOptions = {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ProductName: editProduct.ProductName, ScrumMasterName: editProduct.ScrumMasterName, ProductOwnerName: editProduct.ProductOwnerName,
                                Developers: editProduct.Developers, StartDate: editProduct.StartDate, Methodology: editProduct.Methodology})
        };
        fetch('http://127.0.0.1:3000/api/product/'+product.ProductID,putOptions);
        setEditVis(!editVis);
    };

    return (
        <tr key= {product.ProductID}>
                {editVis ? (
                    <>
                    <td>{product.ProductID}</td>
                    <td><input value={editProduct.ProductName} id="ProductName" onChange={handleChange} required/></td>
                    <td><input value={product.ProductOwnerName} id="ScrumMasterName" onChange={handleChange} required/></td>
                    <td><input value={product.Developers} id="ProductOwnerName" onChange={handleChange} required/></td>
                    <td><input value={product.ScrumMasterName} id="Developers" onChange={handleChange} required/></td>
                    <td><input value={product.StartDate} id="StartDate" onChange={handleChange} required/></td>
                    <td>                
                        <select value={product.Methodology} id="Methodology" onChange={handleChange}>
                            <option value="Agile">Agile</option>
                            <option value="Waterfall">Waterfall</option>
                        </select>
                    </td>
                    <td className='buttonElement'>
                        <button onClick={()=>SubmitEdit({product})}><img src={confirmIcon} alt="Confirm Edit"></img></button>
                    </td>
                    <td className='buttonElement'>
                        <button onClick={()=>ToggleEdit({product})}><img src={exitIcon} alt="Exit Edit"></img></button>
                    </td>
                    </>
                ) : (
                    <>
                    <td>{product.ProductID}</td>
                    <td>{product.ProductName}</td>
                    <td>{product.ProductOwnerName}</td>
                    <td>{product.Developers}</td>
                    <td>{product.ScrumMasterName}</td>
                    <td>{product.StartDate}</td>
                    <td>{product.Methodology}</td>
                    <td className='buttonElement'>
                        <button onClick={()=>ToggleEdit({product})}><img src={editIcon} alt="Edit"></img></button>
                    </td>
                    <td className='buttonElement'>
                        <button onClick={()=>DeleteItem({product})}><img src={deleteIcon} alt="Delete"></img></button>
                    </td>
                    </>
                )}
            </tr> 
    )
};

export default TableElement;

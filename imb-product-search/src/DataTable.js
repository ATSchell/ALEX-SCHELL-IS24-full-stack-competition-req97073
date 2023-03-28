import './DataTable.css';
import React from "react";
import editIcon from './edit_icon.png';
import deleteIcon from './delete_icon.png';

//Function for deleting on click on relevant button 
function DeleteItem({product, tableUpdater}) {
    console.log("Deleting ID:"+product.ProductID);
    const deleteOptions = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    };
    fetch('http://127.0.0.1:3000/api/product/'+product.ProductID,deleteOptions).then(LoadTable(tableUpdater));
};// DeleteItem

//Function for editing on click on relevant button 
function EditItem({product}) {
    console.log("Would open edit interface for ID:");
    console.log(product.ProductID);
};// EditItem

//Get data from API and store using state hook
export const LoadTable = async(setTable) => {
    const resp = await fetch('http://127.0.0.1:3000/api/product');
    // extract json from response and write to table data var
    resp.json().then((repJSON) => {
      setTable(repJSON.products);
    });
    console.log("ran GET request");
}// LoadTable 

//main display of table
function DataTable({tableData, tableUpdater}) {
    return (
    <div className="Scrollable-Table">
      <table>
        <thead>
            <tr>
                <th>Product ID</th>
                <th>Name</th>
                <th>Owner</th>
                <th>Developers</th>
                <th>Scrum Master</th>
                <th>Start Date</th>
                <th>Methodology</th>
                <th colSpan="2"></th>
            </tr>
        </thead>
        <tbody>
            {tableData.map((product, id) => (
            <tr key= {id}>
                <td>{product.ProductID}</td>
                <td>{product.ProductName}</td>
                <td>{product.ProductOwnerName}</td>
                <td>{product.Developers}</td>
                <td>{product.ScrumMasterName}</td>
                <td>{product.StartDate}</td>
                <td>{product.Methodology}</td>
                <td className='buttonElement'>
                    <button onClick={()=>EditItem({product})}><img src={editIcon}></img></button>
                </td>
                <td className='buttonElement'>
                    <button onClick={()=>DeleteItem({product, tableUpdater})}><img src={deleteIcon}></img></button>
                </td>
            </tr> 
            ))}
        </tbody>
        <tfoot><tr><td colSpan="9">Total products retrieved: {tableData.length}</td></tr></tfoot>
        </table>
      </div>
    );
  };


export default DataTable;

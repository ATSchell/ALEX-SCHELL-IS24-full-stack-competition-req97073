import './DataTable.css';
import React from "react";
import editIcon from './edit_icon.png';
import deleteIcon from './delete_icon.png';

function DeleteItem({product}) {
    console.log("would delete ID:");
    console.log(product.ProductID);
};

function EditItem({product}) {
    console.log("Would open edit interface for ID:");
    console.log(product.ProductID);
};

function DataTable({tableData}) {
    return (
    <div className="Scrollable-Table">
      <table>
        <thead>
            <tr>
                <th>Product ID </th>
                <th>Name </th>
                <th>Owner </th>
                <th>Developers </th>
                <th>Scrum Master </th>
                <th>Start Date </th>
                <th>Methodology </th>
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
                    <button onClick={()=>DeleteItem({product})}><img src={deleteIcon}></img></button>
                </td>
            </tr> 
            ))}
        </tbody>
        <tfoot><tr><td colSpan="9">Total products retrived: {tableData.length}</td></tr></tfoot>
        </table>
      </div>
    );
  };


export default DataTable;

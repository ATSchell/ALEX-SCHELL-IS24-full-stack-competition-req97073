import './DataTable.css';
import React, { useEffect } from "react";

import TableElement from './TableElement';

//Get data from API and store using state hook
export const LoadTable = async(setTable) => {
    const resp = await fetch('http://127.0.0.1:3000/api/product');
    // extract json from response and write to table data var
    console.log(resp);
    resp.json().then((repJSON) => {
      setTable(repJSON.products);
    }).then(console.log("ran GET request"));
}// LoadTable 

//main display of table
function DataTable({tableData, tableUpdater, editUpdater}) {
    
    useEffect(() => {
        console.log("table funct called ");
      });

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
            {tableData.map((product, id) => ( <TableElement product={product} id={id}/>))}
        </tbody>
        <tfoot><tr><td colSpan="9">Total products retrieved: {tableData.length}</td></tr></tfoot>
        </table>
      </div>
    );
  };


export default DataTable;

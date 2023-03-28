import {useEffect, useState} from "react";
import './App.css';
import './DataTable'
import HeaderBar from "./Header";
import DataTable from "./DataTable";


function App() {
  // use a state hook to update the table data when needed.
  const [tableData, setTable] = useState([]);

  //Get data from API and store using state hook
  const LoadTable = async() => {
    console.log("ran!");
    const resp = await fetch('http://127.0.0.1:3000/api/product');
    // extract json from response and write to table data var
    resp.json().then((repJSON) => {
      setTable(repJSON.products);
    });
  }//LoadTable 

  // want to have an inital display of data
  useEffect(() => {
    LoadTable();
  }, []);

  return (
    <div className="App">
      <HeaderBar />
      <div className="Table-Holder">
        <div className="Table-Operations">
          <button onClick={LoadTable} className="Refesh-button">Reload Data</button>
          <div className="Search-Bar">
            <input type="text" placeholder="Search for items" className="Search-Input" />
            <button>Search</button>
          </div>
        </div>
        <DataTable tableData={tableData} />
      </div>
    </div>
  );
}//app

export default App;

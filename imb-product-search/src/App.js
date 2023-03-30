import {useEffect, useState} from "react";
import './App.css';
import './components/DataTable'
import HeaderBar from "./components/Header";
import DataTable from "./components/DataTable";
import AddProduct from "./components/AddProduct";
import SearchBar from "./components/SearchBar";
import { LoadTable } from "./components/DataTable";

function App() {
  // use a state hook to update the table data when needed.
  const [tableData, setTable] = useState([]);

  useEffect(() => {
    console.log("table data modified");
  },[tableData])

  // state hook for updating visablity of add component
  const [addVis, setAddVis] = useState(false);

  // toggle the add item form by button
  const ToggleAddDiv = () => {
    setAddVis(!addVis);
  };

  // want to have an inital display of data
  useEffect(() => {
    LoadTable(setTable);
  }, []);

  //render the main component
  return (
    <div className="App">
      <HeaderBar />
      <div className="Table-Holder">
        <div className="Table-Operations">
          <button onClick={()=>ToggleAddDiv()} className="Refesh-button">Add Item</button>
          <button onClick={()=>LoadTable(setTable)} className="Refesh-button">Reload Data</button>
          <SearchBar tableRefresh={setTable}/>
        </div>
        <DataTable tableData={tableData} tableUpdater={setTable}/>
      </div>
      {addVis && (
        <div className="Add-Holder">
          <AddProduct tableLoader={setTable} setVisablity={setAddVis}/>
        </div>
      )}
    </div>
  );
}//app

export default App;

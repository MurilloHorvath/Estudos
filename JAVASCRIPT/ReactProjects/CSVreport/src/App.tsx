import React , { useEffect, useState } from 'react'
import DataGrid from './components/DataGrid'
import MapView from './components/MapView'
//import CSVUploader from './components/CSVUploader'
import Navbar from './Layout/Navbar'
import Footer from './Layout/Footer'

import styles from './App.module.css'

const parseCSV = (text: string) => {
  const [header, ...content] = text.split('\n');
  const allHeaders = header.split(',');
  const data = content.map(line => line.split(','));

  const columnsToKeep = [16,17,84,85,37,38,32]

  const filteredHeaders = columnsToKeep.map(index => allHeaders[index]);
  const filteredData = data.map(row => columnsToKeep.map(index => row[index]));

  const result = {
    header: filteredHeaders,
    data: filteredData
  };
  
  console.log(result)
  return result
}

export default function App() {
  const [csv, setCsv] = useState(null)
  useEffect(() => {
    fetch('../public/2025-01-24 12-14-36 vehicle117.csv')
    .then(r=> r.text())
    .then(text => {
      setCsv(parseCSV(text))
    });
  }, []);

  return (
    <div className={styles.app}>
      <Navbar />
      <div className={styles.content}>
        <MapView csv={csv} />
        <DataGrid csv={csv} />
      </div>
      <Footer />
    </div>
  )
}

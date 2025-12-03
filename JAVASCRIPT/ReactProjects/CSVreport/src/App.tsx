import React , { useEffect, useState } from 'react'
import DataGrid from './components/DataGrid'
import MapView from './components/MapView'
import CSVUploader from './components/CSVUploader'
import Navbar from './Layout/Navbar'
import Footer from './Layout/Footer'

import styles from './App.module.css'

interface CSVData {
  [key: string]: string;
}

interface ProcessedCSV {
  header: string[];
  data: CSVData[];
  fileName: string;
}

export default function App() {
  const [csv, setCsvData] = useState<ProcessedCSV | null>(null);

  const handleCSVData = (csv: ProcessedCSV) => {
    setCsvData(csv);
    //console.log('Dados no App.tsx',csv.header);
    //console.log('Dados no App.tsx',csv.data);
    //console.log('Dados no App.tsx',csv.fileName);
  }

  return (
    <div className={styles.app}>
      <Navbar />
      <div className={styles.content}>
        {!csv ? <CSVUploader onCSVProcessed={handleCSVData}/> : (
          <div>
            <MapView csv={csv} />
            <DataGrid csv={csv} />
          </div>
        )}
      </div>
      <Footer />
    </div>
  )
}

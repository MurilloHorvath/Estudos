import React , { useEffect, useState } from 'react'
import DataGrid from './DataGrid'
import './App.css'

const parseCSV = (text: string) => {
  const [header, ...content] = text.split('\n');
  const allHeaders = header.split(',');

  // Definir quais colunas você quer manter
  //37 - clock.currentTime
  //38 - clock.currentDate
  //84 - gps.lat
  //85 - gps.lon
  //121 - temperature.temperature1
  //122 - temperature.temperature2
  const columnsToKeep = [37, 38, 84, 85, 121, 122]
  const columnsNames = [
    'clock.currentTime',
    'clock.currentDate',
    'gps.lat',
    'gps.lon',
    'temperature.temperature1',
    'temperature.temperature2'
  ]

  // Filtrar os headers
  const filteredHeaders = columnsToKeep.map(index => allHeaders[index]);

  // Filtrar os dados

  const result = {
    header: [],
    data: [],
  };

  const [header, ...content] = text.split('\n');
  result.header = header.split(',');
  content.forEach((item) => {
    result.data.push(item.split(','));
  });
  console.log(result);
  return result;
};
    
export default function App() {
  const [csv, setCsv] = useState(null)
  useEffect(() => {
    fetch('../public/2025-01-24 12-14-36 vehicle117.csv')
    .then(r=> r.text())
    .then(text => {
      setCsv(parseCSV(text));
    });
  }, []);

  return (
    <div className="App">
      <h1>CSV Report Generator</h1>
      <DataGrid csv={csv} />
    </div>
  )
}
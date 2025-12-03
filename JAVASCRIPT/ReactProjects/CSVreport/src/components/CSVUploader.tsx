import React, { useState } from "react";
import Papa from "papaparse"

import styles from './CSVUploader.module.css'

interface CSVData {
  key: string;
}
interface ProcessedCSV {
  header: string[];
  data: CSVData[];
  fileName: string;
}

interface CSVUploaderProps {
    onCSVProcessed: (data: ProcessedCSV) => void;
}

const CSVUploader: React.FC<CSVUploaderProps> = ({ onCSVProcessed }) => {
    const [fileName, setFileName] = useState<string>('');

    const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files?.[0];

        if (file) {
            setFileName(file.name);

            Papa.parse(file, {
                complete: (result) => {
                    const data = result.data as CSVData[];

                    //extrai os headers
                    const header = result.meta.fields || [];

                    const processedData: ProcessedCSV = {
                        header: header,
                        data: data,
                        fileName: file.name
                    }
                    onCSVProcessed(processedData);
                },
                header: true,
                skipEmptyLines:true,
                error: (error) => {
                    console.error('error ao processar o arquivo csv', error);
                    alert('error ao processar o arquivo csv')
                }
            });
        }
    }

    return (
        <div className={styles.container}>
            <h2 className={styles.title}>Upload CSV</h2>
            <div className={styles.fileInputContainer}>
                <input type="file" accept=".csv" onChange={handleFileUpload} className={styles.fileInput} id="file-upload"/>
                <label htmlFor="file-upload" className={styles.fileButton}>
                    <span class="material-symbols-outlined">cloud_upload</span>Upload File
                </label>
            </div>
        </div>
    )
}

export default CSVUploader;
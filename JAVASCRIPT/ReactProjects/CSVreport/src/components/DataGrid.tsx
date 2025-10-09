import React from "react";
import styles from './DataGrid.module.css'

const DataGrid = ({ csv }) => {
    if (!csv) {
        return (
            <div>
                <p>Carregando...</p>
            </div>
        );
    }

    // Função para converter HH:MM:SS para segundos
    const timeToSeconds = (timeStr) => {
        if (!timeStr || timeStr === '--:--:--' || timeStr === '00:00:00') return 0;
        
        try {
            const parts = timeStr.split(':');
            if (parts.length !== 3) return 0;
            
            const hours = parseInt(parts[0], 10);
            const minutes = parseInt(parts[1], 10);
            const seconds = parseInt(parts[2], 10);
            
            if (isNaN(hours) || isNaN(minutes) || isNaN(seconds)) return 0;
            
            return (hours * 3600) + (minutes * 60) + seconds;
        } catch (error) {
            console.error('Error parsing time:', timeStr, error);
            return 0;
        }
    };

    // Função para formatar segundos para HH:MM:SS
    const secondsToTime = (totalSeconds) => {
        const hours = Math.floor(totalSeconds / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        const seconds = totalSeconds % 60;

        return `${hours.toString().padStart(1,'0')}h ${minutes.toString().padStart(1, '0')}m ${seconds.toString().padStart(1, '0')}s`;
    };

    const flightData = csv.data
    .map(row => ({
        distance: parseFloat(row['flightDistance']),
        duration: timeToSeconds(row['flightTime']),
        daytime: row['clock.currentTime'],
        daydate: row['clock.currentDate'],
        consume: parseFloat(row['battery0.percentRemaining'])
    })).filter(item => item.duration > 0); // filtrar apenas duracoes validas

    // Encontrar a maior distância
    const flightDistance = Math.max(...flightData.map(d => d.distance));

    // Formatar dia do voo
    const flightDay = flightData.map(d => d.daydate)[0]; // Pega o dia do primeiro registro

    // Formatar hora do voo
    const flightTime = flightData.map(d => d.daytime)[0].slice(0,5); // Pega a hora do primeiro registro

    // Encontrar o consumo total de bateria
    const totalConsume = ((Math.max(...flightData.map(d => d.consume)) - Math.min(...flightData.map(d => d.consume))) + '%');

    // Encontrar a maior duração em segundos
    const maxDurationSeconds = Math.max(...flightData.map(d => d.duration));

    // Converter de volta para formato de tempo
    const maxDurationFormatted = secondsToTime(maxDurationSeconds);
    
    return (
        <div className={styles.dataGrid}>
            <h1 className={styles.title}>Informações do Voo</h1>
            <p className={styles.date}>{flightDay}, {flightTime}</p>
            <div className={styles.grid}>
                <div>
                    <p className={styles.value}>{flightDistance}m</p>
                    <h2 className={styles.subtitle}>Distância Voada</h2>
                </div>
                <div>
                    <p className={styles.value}>{maxDurationFormatted}</p>
                    <h2 className={styles.subtitle}>Tempo Total Voando</h2>
                </div>
                <div>
                    <p className={styles.value}>{totalConsume}</p>
                    <h2 className={styles.subtitle}>Consumo Total de Bateria</h2>
                </div>
            </div>
        </div>
    )
}

export default DataGrid;

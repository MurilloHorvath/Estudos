import styles from "./History.module.css"

import regissobak from "../../public/regissobak.jpg"

function History(){
    return(
        <div className={styles.history}>
            <h2 className={styles.historyTitle}>Nossa Historia</h2>
            <div className={styles.biography}>
                <img className={styles.biographyImage} src={regissobak} alt="Regissobak" />
                <div className={styles.biographyText}>
                    <p className={styles.biographyParagraph}>A história do Pastor Regis Sobak é a semente da qual nasceu o Projeto Casa Recomeçar. 
                    Criado em uma comunidade assolada pelo tráfico de drogas, Regis conheceu de perto a falta de oportunidades 
                    e os caminhos difíceis que se abrem para as crianças sem apoio. Ele próprio enfrentou o vício e a vida nas ruas, 
                    mas encontrou na sua fé e na palavra de Deus a força para uma transformação radical.</p>
                    <p className={styles.biographyParagraph}>Dessa superação pessoal surgiu um propósito maior: impedir que outras crianças repitam esse ciclo. 
                    Assim, fundou o Projeto Casa Recomeçar, um espaço de acolhimento, esperança e novas possibilidades, 
                    para que a história dessas crianças seja de conquistas, e não de perdas.</p>
                </div>
            </div>
        </div>  
    )
}

export default History
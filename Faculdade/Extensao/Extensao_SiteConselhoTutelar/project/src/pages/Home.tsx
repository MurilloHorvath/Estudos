import { Link } from "react-router-dom"

import styles from "./Home.module.css"

function Home(){
    return(
        <div className={styles.home}>
            <h2 className={styles.homeTitle}>Conselho Tutelar 2 Sarandi</h2>
            <p className={styles.homeDescription}>O Conselho Tutelar é um órgão autônomo e permanente responsável por zelar pelos direitos das crianças e adolescentes, conforme o Estatuto da Criança e do Adolescente (ECA).</p>
            <p className={styles.homeDescription}>Nosso compromisso é garantir proteção, orientação e apoio às famílias, atuando sempre em parceria com a comunidade, escolas, órgãos de saúde, Ministério Público e demais instituições.</p>
            <p className={styles.homeDescription}>Atendemos toda a região de Sarandi com foco em prevenir e combater situações de risco, assegurando que cada criança e adolescente tenha seus direitos respeitados.</p>
            <Link to="/Contact">Contatos</Link>
        </div>
    )
}

export default Home
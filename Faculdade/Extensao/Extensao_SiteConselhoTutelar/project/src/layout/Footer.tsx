import Container from "./Container"

import styles from "./Footer.module.css"

import assin from "../assets/imagem-legal.jpg"

function Footer() {
    return(
        <footer className={styles.footer}>
            <img src={assin} alt="img" className={styles.assin}/>
            <p className={styles.text}>Site desenvolvido por Murillo Silveira Horvath</p>
        </footer>
    )
}

export default Footer
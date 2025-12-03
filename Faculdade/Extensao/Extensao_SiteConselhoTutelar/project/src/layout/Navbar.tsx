import { Link } from "react-router-dom"

import Container from "./Container"

import styles from "./Navbar.module.css"

import logo from "../../public/logoicon.png"

function Navbar() {
    return(
        <nav className={styles.navbar}>
            <Container>
                <img src={logo} alt="" className={styles.logo}/>
                <div>
                    <h1 className={styles.title1}>PROJETO CASA</h1>
                    <h1 className={styles.title2}><p className={styles.redtitle}>Re</p>começar</h1>
                </div>
                    <ul className={styles.list}>
                        <li className={styles.item}>
                            <Link to="/">Inicio</Link>
                        </li>
                        <li className={styles.item}>
                            <Link to="/History">Historia</Link>
                        </li>
                        <li className={styles.item}>
                            <Link to="/Services">Serviços</Link>
                        </li>
                        <li className={styles.item}>
                            <Link to="/Contact">Contatos</Link>
                        </li>
                    </ul>
            </Container>
        </nav>
    )
}

export default Navbar
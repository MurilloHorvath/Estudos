import { Link } from "react-router-dom"

import Container from "./Container"

import styles from "./Navbar.module.css"

import logo from "../../public/logo.png"
//import logo from "../../public/Conselho-Tutelar-Logo-Vector/ConselhoTutelarLogoVector.svg"
//import logo from "../../public/"

function Navbar() {
    return(
        <nav className={styles.navbar}>
            <Container>
                <img src={logo} alt="" className={styles.logo}/>
                <h1 className={styles.title}>Conselho Tutelar</h1>
                    <ul className={styles.list}>
                        <li className={styles.item}>
                            <Link to="/">Inicio</Link>
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
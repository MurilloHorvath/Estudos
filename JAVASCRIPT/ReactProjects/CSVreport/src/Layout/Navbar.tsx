import styles from './Navbar.module.css';

import logo from '../assets/skydroneslogo.png';
import Container from './Container';

export default function Navbar() {
    return(
        <nav className={styles.navbar}>
            <Container>
                <img className={styles.logo} src={logo} alt="Logo SkyDrones" />
            </Container>
        </nav>
    )
}


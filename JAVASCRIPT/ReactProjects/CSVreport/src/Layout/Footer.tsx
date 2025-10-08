import styles from './Footer.module.css';

import logofooter from '../assets/skydronesfooter.png';

export default function Footer() {
    return (
        <footer className={styles.footer}>
                <img className={styles.logofooter} src={logofooter} alt="Logo SkyDrones" />
                <p className={styles.copy}>© 2025 SkyDrones. All rights reserved.</p>
        </footer>
    )
}
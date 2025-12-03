import { Link } from "react-router-dom"
import { useState } from "react";
import Container from "./Container"
import styles from "./Navbar.module.css"
import logo from "../../public/logoicon.png"


function Navbar() {
    const [sidebarOpen, setSidebarOpen] = useState(false);
    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };
    const closeSidebar = () => {
        setSidebarOpen(false);
    };

    return(
    <>
        <nav className={styles.navbar}>
            <Container>
                <div className={styles.divTitle}>
                    <img src={logo} alt="Logo do Projeto Casa Recomeçar" className={styles.logo}/>
                    <div className={styles.divTitleText}>
                        <h1 className={styles.title1}>PROJETO CASA</h1>
                        <h1 className={styles.title2}><p className={styles.redtitle}>Re</p>começar</h1>
                    </div>
                </div>
                <div className={styles.divMenu}>
                    <button className={`${styles.menuButton} ${sidebarOpen ? styles.active : ''}`}
                    onClick={toggleSidebar}
                    aria-label="Abrir menu">
                        <span className={styles.menuicon}></span>
                        <span className={styles.menuicon}></span>
                        <span className={styles.menuicon}></span>
                    </button>
                    <ul className={styles.desktopMenu}>
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
                </div>
            </Container>
        </nav>
    <div className={`${styles.sidebarOverlay} ${sidebarOpen ? styles.active : ''}`} onClick={closeSidebar}></div>
      
      <aside className={`${styles.sidebar} ${sidebarOpen ? styles.active : ''}`}>
        <div className={styles.sidebarHeader}>
          <button className={styles.closeButton} onClick={closeSidebar} aria-label="Fechar menu">
            ×
          </button>
        </div>
        
        <div className={styles.sidebarContent}>
          <ul className={styles.sidebarMenu}>
            <li className={styles.sidebarItem}>
              <Link to="/" onClick={closeSidebar}>Inicio</Link>
            </li>
            <li className={styles.sidebarItem}>
              <Link to="/History" onClick={closeSidebar}>Historia</Link>
            </li>
            <li className={styles.sidebarItem}>
              <Link to="/Services" onClick={closeSidebar}>Serviços</Link>
            </li>
            <li className={styles.sidebarItem}>
              <Link to="/Contact" onClick={closeSidebar}>Contatos</Link>
            </li>
          </ul>
        </div>
      </aside>
    </>
    )
}

export default Navbar
import styles from "./Services.module.css"

function Services() {
    return(
        <div className={styles.services}>
            <h2 className={styles.servicesTitle}>O que fazemos</h2>
            <p className={styles.servicesDescription}>O Projeto Casa Recomeçar atua em situações que envolvem ameaça ou violação dos direitos de crianças e adolescentes, tais como:</p>
            <ul className={styles.servicesList}>
                <li className={styles.servicesListItem}>Negligência, abandono ou maus-tratos</li>
                <li className={styles.servicesListItem}>Violência física, psicológica ou sexual</li>
                <li className={styles.servicesListItem}>Situação de rua ou trabalho infantil</li>
                <li className={styles.servicesListItem}>Desrespeito ao direito à educação e saúde</li>
            </ul>
            <p className={styles.servicesDescription}>Nossos principais serviços incluem:</p>
            <ul className={styles.servicesList}>
                <li className={styles.servicesListItem}>Atendimentos e orientações a famílias</li>
                <li className={styles.servicesListItem}>Encaminhamentos para órgãos competentes (saúde, assistência social, Ministério Público etc.)</li>
                <li className={styles.servicesListItem}>Acompanhamento de casos de risco</li>
                <li className={styles.servicesListItem}>Ações de prevenção e orientação à comunidade</li>
            </ul>
            <p className={styles.servicesDescription}>O Projeto Casa Recomeçar não é órgão de denúncia anônima, mas recebe e encaminha casos.</p>
            <p className={styles.servicesDescription}>Para emergências, ligue 190 (Polícia Militar) ou 100 (Disque Direitos Humanos).</p>
        </div>
    )
}

export default Services
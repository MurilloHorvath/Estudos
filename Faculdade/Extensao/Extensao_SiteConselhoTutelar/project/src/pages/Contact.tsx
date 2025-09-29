import styles from './Contact.module.css'

function Contact() {
    return(
        <div className={styles.contact}>
            <h2 className={styles.contactTitle}>Fale conosco</h2>
            <p className={styles.contactDescription}>Estamos à disposição para atendimento e orientações.</p>
            <p className={styles.contactDescription}>Você pode entrar em contato pelos seguintes canais:</p>
            <ul className={styles.contactList}>
                <li className={styles.contactListItem}>Endereço: R. Jackson de Figueiredo, 731 - Sarandi, Porto Alegre - RS, 91120-380</li>
                <li className={styles.contactListItem}>Telefone: (51) 3289-2012</li>
                <li className={styles.contactListItem}>E-mail: ct2@portoalegre.rs.gov.br</li>
                <li className={styles.contactListItem}>Horário de funcionamento: segunda a sexta, das 8h às 18h</li>
            </ul>
        </div>
    )
}

export default Contact
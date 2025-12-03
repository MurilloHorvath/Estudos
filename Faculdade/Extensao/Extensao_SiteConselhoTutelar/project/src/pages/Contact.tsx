import styles from './Contact.module.css'

function Contact() {
    return(
        <div className={styles.contact}>
            <h2 className={styles.contactTitle}>Fale conosco</h2>
            <p className={styles.contactDescription}>Estamos à disposição para atendimento e orientações.</p>
            <p className={styles.contactDescription}>Você pode entrar em contato pelos seguintes canais:</p>
            <ul className={styles.contactList}>
                <li className={styles.contactListItem}>Endereço: Bairro Reforma em Itapua</li>
                <li className={styles.contactListItem}>Telefone: (51) 99490-9615</li>
                <li className={styles.contactListItem}>E-mail: projetocasarecomecar@gamil.com</li>
                <li className={styles.contactListItem}>Instagram: @projetocasarecomecar</li>
            </ul>
        </div>
    )
}

export default Contact
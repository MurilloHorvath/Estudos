import { BsFacebook,BsInstagram,BsLinkedin } from "react-icons/bs";

import styles from './Footer.module.css'

function Footer() {
    return (
        <ul className={styles.social_list}>
            <li><BsFacebook/></li>
            <li><BsInstagram/></li>
            <li><BsLinkedin/></li>
        </ul>
    )
}

export default Footer
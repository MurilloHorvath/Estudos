import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Navbar from "./layout/Navbar"
import Footer from "./layout/Footer"
import Container from "./layout/Container"
import Home from "./pages/Home"
import History from "./pages/History"
import Services from "./pages/Services"
import Contact from "./pages/Contact"

function App() {
  return (
    <Router>
      <Navbar />
      <Container>
        <Routes>
          <Route path="/" element={<Home/>} ></Route>
          <Route path="/History" element={<History/>} ></Route>
          <Route path="/Services" element={<Services/>} ></Route>
          <Route path="/Contact" element={<Contact/>} ></Route>
        </Routes>
      </Container>
      <Footer />
    </Router>
  )
}

export default App

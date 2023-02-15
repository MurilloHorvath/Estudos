import './App.css';
// import HelloWorld from './components/HelloWorld'
// import SayMyName from './components/SayMyName'

// import Pessoa from './components/Pessoa'
// import List from './components/List'

// import Evento from './components/Evento'
// import Form from './components/Form'

// import Condicional from './components/Condicional';

// import OutraLista from './components/OutraLista';

// import SeuNome from './components/SeuNome';
// import Saudacao from './components/Saudacao';

import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Home from './pages/Home';
import Contato from './pages/Contato';
import Empresa from './pages/Empresa';
import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer';

// import { useState } from 'react';

function App() {

  // const [seuNome, setSeuNome] = useState()

  // const meusItens = ["React", "Vue", "Angular"]

  // const nome = "Jasmin"

  return (
    // <div className="App">
    //   <HelloWorld />
    //   <SayMyName nome="Murillo"/>
    //   <SayMyName nome={nome}/>

    //   <Pessoa nome="Murillo" idade="19" profissao="Técnico em eletrônica" foto="https://via.placeholder.com/150" />
    //   <List/>

    //   <h1>Testando evento</h1>
    //   <Evento numero="1" />
    //   <Form/>

    //   <h1>Renderização Condicional</h1>
    //   <Condicional/>

    //   <h1>Renderização de Listas</h1>
    //   <OutraLista itens={meusItens} />
    //   <OutraLista itens={[]} />

    //   <h1>State Lift</h1>
    //   <SeuNome setNome={setSeuNome}/>
    //   <Saudacao nome={seuNome} />
    // </div>

      <Router>
        <Navbar />
        <Routes>
          <Route exact path="/" element={<Home />} ></Route>
          <Route path="/empresa" element={<Empresa />} ></Route>
          <Route path="/contato" element={<Contato />} ></Route>
        </Routes>
        <Footer />
      </Router>

  )
}

export default App;

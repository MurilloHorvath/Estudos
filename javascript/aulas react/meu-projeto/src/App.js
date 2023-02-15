import './App.css';
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName'
import Pessoa from './components/Pessoa'
import List from './components/List'
import Evento from './components/Evento'
import Form from './components/Form'

function App() {

  const nome = "Jasmin"

  return (
    <div className="App">
      <HelloWorld />
      <SayMyName nome="Murillo"/>
      <SayMyName nome={nome}/>
      <Pessoa nome="Murillo" idade="19" profissao="Técnico em eletrônica" foto="https://via.placeholder.com/150" />
      <List/>
      <h1>Testando evento</h1>
      <Evento numero="1" />
      <Evento numero="2" />
      <Form/>
    </div>
  )
}

export default App;

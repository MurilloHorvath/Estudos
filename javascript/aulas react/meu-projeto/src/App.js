import './App.css';
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName'
import Pessoa from './components/Pessoa'

function App() {

  const nome = "Jasmin"

  return (
    <div className="App">
      <HelloWorld />
      <SayMyName nome="Murillo"/>
      <SayMyName nome={nome}/>
      <Pessoa nome="Murillo" idade="19" profissao="Técnico em eletrônica" foto="https://via.placeholder.com/150" />
    </div>
  )
}

export default App;

import React from 'react';
import './App.css'
import { HashRouter, Routes , Route } from 'react-router-dom';
import { AuthProvider } from './Context/AuthContext';

//--------------
import Home from './Components/Home'
import Login from './Components/Login'
import SignUpPage from './Components/SignUp'
import Activate from './Components/Activate'
import ConfirmReset from './Components/ConfirmReset'
import Navbar from './Components/Navbar'
import Footer from './Components/Footer';

//----------------------------------
let generalCSS={
  backgroundColor:'#dae0e6'
}
//--------------------------------------
function App() {
  return (
    <div className="App" style={generalCSS}>
      <HashRouter>
        <AuthProvider>
          <Navbar/>
          <Routes>  
            <Route  path='/' element={<Home/>}/>
            <Route  path='/login' element={<Login/>}/>
            <Route exact path='/signup' element={<SignUpPage/>}/>
            <Route exact path='/password_reset/confirm/:uid/:token/' element={<ConfirmReset/>}/>
            <Route exact path='/activate/:uid/:token' element={<Activate/>}/>  
          </Routes>
          <Footer/>
        </AuthProvider>
      </HashRouter>

    </div>
  );
}

export default App;

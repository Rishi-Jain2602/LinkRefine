import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import Review from './components/Review'
import Upload from './components/Upload'
function App() {
  return (
    <>
      <Router>
        <Navbar/>
        <Routes>
          <Route path='/' element = {<Home/>} />
          <Route path='/upload' element = {<Upload/>} />
          <Route path='/review' element = {<Review/>} />
        </Routes>
      </Router>
    </>
  );
}

export default App;

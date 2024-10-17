// src/components/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from '../pages/Login';
import NewRecipe from '../pages/NewRecipe';
import RecipeList from '../pages/RecipeList';
import NavBar from './NavBar';

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/new-recipe" element={<NewRecipe />} />
        <Route path="/recipes" element={<RecipeList />} />
        {/* You can add a redirect or a default route here if needed */}
      </Routes>
    </Router>
  );
}

export default App;

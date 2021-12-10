import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Nav from './components/Nav'
import PostList from './components/PostList'
import PostShow from './components/PostShow'
import Home from './pages/Home'
import Login from './components/Login'
import NotFound from './components/NotFound'
import { getToken } from './helpers/auth'
import { useEffect, useState } from 'react'
import Register from './components/Register'

import axios from 'axios'
import Message from './components/Message'
import { getUserId } from './helpers/auth'


function App({ id }) {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [users, setUsers] = useState([]) 

  useEffect(() => {
    if (getToken()) {
      setIsLoggedIn(true)
    } else {
      setIsLoggedIn(false)
    }
  }, [])


  function UserLogIn(props) {
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    useEffect(() => {
      if (getToken()) {
        setIsLoggedIn(true)
      } else {
        setIsLoggedIn(false)
      }
    }, [])

    return (
      <Login {...props} isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
    )
  }

  useEffect(() => {
    const getData = async () => {
      const res = await axios.get('/api/auth/') 
      console.log(res.data)
      setUsers(res.data)
    }
    getData()
  }, [])

  id = getUserId(id)
  console.log(id)

  return (
    <>
      <Router>
        <Nav isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
        <Routes>
          {users.map((user, index) => (
            <Route key={index} path={`/:${id}/${user.username}`} element={<Message />} />
          ))}
          <Route path='/' element={<Home />} />
          <Route path='/posts' element={<PostList />} />
          <Route path='/posts/:id' element={<PostShow />} />
          <Route path='/login' element={<UserLogIn />} />
          <Route path='/register' element={<Register />} />
          <Route element={<NotFound />} />
        </Routes>
      </Router>
    </>
  )
}

export default App

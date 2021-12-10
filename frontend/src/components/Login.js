// import axios from 'axios'
import React from 'react'
import { useState } from 'react'
import { setToken, setUserId } from '../helpers/auth'
import { useNavigate } from 'react-router'
// import { getAxiosRequestConfig } from '../helpers/api'
import FormInput from './FormInput'
// import { login } from '../helpers/api'
import axios from 'axios'
// import App from '../App'


const Login = ({ setIsLoggedIn }) => {
  const [data, setData] = useState({
    username: '',
    password: '',
  })

  const [errorInfo, setErrorInfo] = useState({})
  const [isError, setIsError] = useState(false)
  const navigate = useNavigate()


  const handleSubmit = async (event) => {
    event.preventDefault()
    
    const config = {
      method: 'post',
      url: 'http://localhost:8000/api/auth/login/',
      headers: { 
        'Content-Type': 'application/json',
      },
      data: data,
    }
    
    try {
      const response = await axios(config).catch(handleError)
      setToken(response.data.token)
      console.log(response.data)
      setUserId(response.data.id[0])
      console.log(response.data.id[0])
      setIsLoggedIn(true)
      setIsError(false)
      navigate('/posts')
    } catch (err) {
      console.log(err)
      setIsError(true)
    }
  }

  const handleError = (error) => {
    if (error.response) {
      setErrorInfo(error.response.data)
      setIsError(true)
    }
  }

  const handleFormChange = (event) => {
    const { name, value } = event.target
    setData({
      ...data,
      [name]: value,
    })
    console.log(data)
  }

  const formInputProps = { data, errorInfo, handleFormChange }
  
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h1>Login to SlackOverflow</h1>
        <FormInput
          placeholder='username'
          type='text'
          name='username'
          {...formInputProps}
        />
        <FormInput
          placeholder='password'
          type='password'
          name='password'
          {...formInputProps}
        />
        <div>
          <input type='submit' value='Login' />
        </div>
        {isError ? (
          <div className='error'>
            <p>Incorrect Details Provided</p>
          </div>
        ) : (
          <></>
        )}
      </form>
    </div>
  )
}

export default Login
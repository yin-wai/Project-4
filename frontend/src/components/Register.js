import axios from 'axios'
import React from 'react'
import { useState } from 'react'
import { useNavigate } from 'react-router'
// import { getAxiosRequestConfig } from '../helpers/api'
import { setToken } from '../helpers/auth'
import FormInput from './FormInput'

const Register = () => {
  const navigate = useNavigate()
  const [isError, setIsError] = useState(false)

  const [data, setData] = useState({
    username: '',
    email: '',
    password: '',
    password_confirmation: '',
    image: '',
  })

  

  const [errorInfo, setErrorInfo] = useState({})


  const handleSubmit = async (event) => {
    event.preventDefault()
    
    const config = {
      method: 'post',
      url: 'http://localhost:8000/api/auth/register/',
      headers: { 
        'Content-Type': 'application/json',
      },
      data: data,
    }
    
    try {
      const response = await axios(config).catch(handleError)
      setToken(response.data.token)
      setIsError(false)
      navigate('/login')
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
    <section>
      <form onSubmit={handleSubmit}>
        <h1>Register to Slack Overflow</h1>
        <FormInput
          placeholder='username'
          type='text'
          name='username'
          {...formInputProps}
        />
        <FormInput
          placeholder='email@email.com'
          type='text'
          name='email'
          {...formInputProps}
        />
        <FormInput
          placeholder='password'
          type='password'
          name='password'
          {...formInputProps}
        />
        <FormInput
          placeholder='password confirmation'
          type='password'
          name='password_confirmation'
          {...formInputProps}
        />
        <div>
          <input type='submit' value='Register' />
        </div>
        {isError ? (
          <div className='error'>
            <p>Error! Please try again</p>
          </div>
        ) : (
          <></>
        )

        }
      </form>
    </section>
  )
}

export default Register
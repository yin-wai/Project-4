import axios from 'axios'
import React from 'react'
// import { getAxiosRequestConfig } from '../helpers/api'
import { useNavigate } from 'react-router'
import { useState } from 'react'
import FormInput from './FormInput'
import { getToken, getUserId } from '../helpers/auth'

const PostAdd = () => {
  const [data, setData] = useState({
    text: '',
    author: parseInt(`${getUserId()}`),
  })

  const [errorInfo, setErrorInfo] = useState({})
  const [isError, setIsError] = useState(false) 
  
  const navigate = useNavigate()

  const handleError = (error) => {
    if (error.response) {
      setErrorInfo(error.response.data)
      setIsError(true)
    }
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    console.log(getToken())
    const config = {
      method: 'post',
      url: 'http://localhost:8000/api/posts/',
      headers: { 
        Authorization: `Bearer ${getToken()}`, 
        'Content-Type': 'application/json',
      },
      data: data,
    }
    
    console.log(data)

    try {
      const response = await axios(config).catch(handleError)
      console.log(response.data)
      setIsError(false)
      navigate('/posts')
    } catch (err) {
      console.log(err)
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
    <form onSubmit={handleSubmit}>
      <h1>Add A Post</h1>
      <FormInput
        name="text"
        type="text"
        placeholder="type whats on your mind"
        {...formInputProps}
      />
      <div>
        <input type='submit' value='Add Post' />
      </div>
      {isError ? (
        <div className='error'>
          <p>Incorrect Details Provided</p>
        </div>
      ) : (
        <></>
      )}
    </form>
  )
}
export default PostAdd

import { useState, useEffect } from 'react'
import axios from 'axios'
import { useParams } from 'react-router'
import PostAdd from './PostAdd'

const PostShow = () => {
  const [posts, setPosts] = useState([])
  const { id } = useParams()

  useEffect(() => {
    const getData = async () => {
      const res = await axios.get(`/api/posts/${id}`) // * <-- replace with your endpoint
      console.log(res.data)
      setPosts(res.data)
    }
    getData()
  }, [id])

  console.log(posts)

  return (
    <div>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>
            {post.text}
          </li>
        ))}
      </ul>
      <PostAdd />
    </div>
  )


}

export default PostShow
import { useState, useEffect } from 'react'
import axios from 'axios'
import PostAdd from './PostAdd'

const PostList = () => {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    const getData = async () => {
      const res = await axios.get('/api/posts/') // * <-- replace with your endpoint
      console.log(res.data)
      setPosts(res.data)
    }
    getData()
  }, [])

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

export default PostList
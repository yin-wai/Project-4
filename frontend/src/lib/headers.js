import Cookies from 'js-cookie'
const csrftoken = Cookies.get('csrftoken')
import { getToken } from '..auth.js'

export const headers = {
    common: {
        'X-CSRF-TOKEN': csrftoken
    },
    headers: {Authorization: `Bearer ${getToken()}`}
}
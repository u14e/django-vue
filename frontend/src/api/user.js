import axios from 'axios'

export function fetch_code (phone) {
  const url = '/api/verify-code/'

  return axios.post(url, {
    phone
  }).then(res => {
    return Promise.resolve(res.data)
  }).catch(error => {
    const res = error.response
    if (res) {
      console.error(res.status)
      console.error(res.data)
      const first_err = Object.values(res.data)
      alert(first_err[0][0])
      throw first_err[0][0]
    }
  })
}

export function register (data) {
  const url = '/api/register/'

  return axios.post(url, data).then(res => {
    return Promise.resolve(res.data)
  }).catch(error => {
    const res = error.response
    if (res) {
      console.error(res.status)
      console.error(res.data)
      const first_err = Object.values(res.data)
      alert(first_err[0][0])      
      throw first_err[0][0]
    }
  })
}

export function login (data) {
  const url = '/api/login/'

  return axios.post(url, data).then(res => {
    return Promise.resolve(res.data)
  }).catch(error => {
    const res = error.response
    if (res) {
      console.error(res.status)
      console.error(res.data)
      const first_err = Object.values(res.data)
      alert(first_err[0][0])      
      throw first_err[0][0]
    }
  })
}

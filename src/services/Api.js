import axios from 'axios'


const Api = ({
    baseURL,
    noHeaders,
    headers,
    options,
}) => {
    const sessionToken = null

    const generateHeaders = () => {
        if (!noHeaders) {
            return {
                authorization: `Bearer ${sessionToken}`,
                ...headers,
            }
        }
        return {
            ...headers,
        }
    }

    const baseApiUrl = process.env.VUE_APP_API
    const newInstance = axios.create({
        baseURL: baseURL || baseApiUrl,
        headers: generateHeaders(),
        ...options,
    })

    newInstance.interceptors.response.use(undefined, function (err) {
        return new Promise(function (resolve, reject) {
            if (err.response.status === 401) {
                localStorage.removeItem('user')
                localStorage.removeItem('token')
                window.location.reload()
            } else if (err.response) {
                reject(err)
            }
        })
    })

    return newInstance
}

export default Api
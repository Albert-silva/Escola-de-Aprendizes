import axios from 'axios'


const Api = () => {
    const sessionToken = localStorage.getItem('token');

    const baseApiUrl = process.env.VUE_APP_API
    const newInstance = axios.create({
        baseURL: baseApiUrl,
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
            'token': sessionToken
        }
    });

    // newInstance.interceptors.response.use(undefined, function (err) {
    //     return new Promise(function (resolve, reject) {
    //         if (err.response.status === 401) {
    //             localStorage.removeItem('user')
    //             localStorage.removeItem('token')
    //             window.location.reload()
    //         } else if (err.response) {
    //             reject(err)
    //         }
    //     })
    // })

    return newInstance;
}

export default Api;
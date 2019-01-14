const API_URL = 'http://localhost:8000/api';

export function getToken() {
    return localStorage.getItem('token');
}

export function get(url) {
    return fetch(`${API_URL}${url}`, {
      headers: new Headers({
        'Authorization': `Token ${getToken()}`,
      }),
      method: 'GET',
    }).then(response =>
        response.json()
          .then(data => ({
            ok: response.ok,
            status: response.status,
            statusText: response.statusText,
            type: response.type,
            data,
          }))
          .catch(error => console.warn(error))
    );
  }

  export function put(url, body) {
    return fetch(`${API_URL}${url}`, {
      headers: new Headers({
        'Authorization': `Token ${getToken()}`,
        'Accept': 'application/json',
        'Content-Type':'application/json'
      }),
      method: 'PUT',
      body: body
    })
  }

  export function post(url, body) {
    return fetch(`${API_URL}${url}`, {
      headers: new Headers({
        'Authorization': `Token ${getToken()}`,
        'Accept': 'application/json',
        'Content-Type':'application/json'
      }),
      method: 'post',
      body: body
    })
  }
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
          .then(console.warn('Bad Request'))
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

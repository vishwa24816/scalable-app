const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

export async function login(email: string, password: string) {
  const response = await fetch(`${API_URL}/user/token/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    throw new Error('Login failed');
  }

  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  localStorage.setItem('refresh_token', data.refresh);
  return data;
}

export async function register(email: string, password: string, name: string) {
  const response = await fetch(`${API_URL}/user/create/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password, name }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Registration failed');
  }

  return await response.json();
}

export async function getProfile() {
  const accessToken = localStorage.getItem('access_token');
  if (!accessToken) throw new Error('No access token');

  const response = await fetch(`${API_URL}/user/me/`, {
    method: 'GET',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
    },
  });

  if (!response.ok) {
    throw new Error('Failed to fetch profile');
  }

  return await response.json();
}

export async function logout() {
  const refreshToken = localStorage.getItem('refresh_token');
  const accessToken = localStorage.getItem('access_token');

  if (refreshToken) {
    await fetch(`${API_URL}/user/logout/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${accessToken}`,
      },
      body: JSON.stringify({ refresh: refreshToken }),
    });
  }

  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
}

export async function refreshToken() {
  const refresh = localStorage.getItem('refresh_token');
  if (!refresh) throw new Error('No refresh token available');

  const response = await fetch(`${API_URL}/user/token/refresh/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh }),
  });

  if (!response.ok) {
    throw new Error('Refresh failed');
  }

  const data = await response.json();
  localStorage.setItem('access_token', data.access);
  return data.access;
}

import { login, logout, refreshToken } from '../auth';

// Mock fetch
global.fetch = jest.fn();

describe('Auth Service', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    localStorage.clear();
  });

  it('login calls the API and stores tokens', async () => {
    const mockResponse = {
      access: 'access-token',
      refresh: 'refresh-token',
    };
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    });

    const result = await login('test@example.com', 'password123');

    expect(global.fetch).toHaveBeenCalledWith(
      expect.stringContaining('/api/user/token/'),
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ email: 'test@example.com', password: 'password123' }),
      })
    );
    expect(result).toEqual(mockResponse);
    expect(localStorage.getItem('access_token')).toBe('access-token');
    expect(localStorage.getItem('refresh_token')).toBe('refresh-token');
  });

  it('logout blacklists token and clears storage', async () => {
    localStorage.setItem('access_token', 'access-token');
    localStorage.setItem('refresh_token', 'refresh-token');
    
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
    });

    await logout();

    expect(global.fetch).toHaveBeenCalledWith(
      expect.stringContaining('/api/user/logout/'),
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ refresh: 'refresh-token' }),
      })
    );
    expect(localStorage.getItem('access_token')).toBeNull();
    expect(localStorage.getItem('refresh_token')).toBeNull();
  });

  it('refreshToken fetches new access token', async () => {
    localStorage.setItem('refresh_token', 'refresh-token');
    const mockResponse = { access: 'new-access-token' };
    
    (global.fetch as jest.Mock).mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    });

    const result = await refreshToken();

    expect(global.fetch).toHaveBeenCalledWith(
      expect.stringContaining('/api/user/token/refresh/'),
      expect.objectContaining({
        method: 'POST',
        body: JSON.stringify({ refresh: 'refresh-token' }),
      })
    );
    expect(result).toBe('new-access-token');
    expect(localStorage.getItem('access_token')).toBe('new-access-token');
  });
});

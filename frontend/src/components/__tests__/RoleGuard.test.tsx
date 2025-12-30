import React from 'react';
import { render, screen } from '@testing-library/react';
import { RoleGuard } from '../RoleGuard';
import { useAuth } from '../../context/AuthContext';

jest.mock('../../context/AuthContext');

describe('RoleGuard', () => {
  it('renders children if user has required role', () => {
    (useAuth as jest.Mock).mockReturnValue({
      user: { role: 'SYSTEM_ADMINISTRATOR' },
      isLoading: false,
    });

    render(
      <RoleGuard allowedRoles={['SYSTEM_ADMINISTRATOR']}>
        <div data-testid="protected">Protected Content</div>
      </RoleGuard>
    );

    expect(screen.getByTestId('protected')).toBeInTheDocument();
  });

  it('renders nothing if user does not have required role', () => {
    (useAuth as jest.Mock).mockReturnValue({
      user: { role: 'GENERAL_USER' },
      isLoading: false,
    });

    render(
      <RoleGuard allowedRoles={['SYSTEM_ADMINISTRATOR']}>
        <div data-testid="protected">Protected Content</div>
      </RoleGuard>
    );

    expect(screen.queryByTestId('protected')).not.toBeInTheDocument();
  });
});

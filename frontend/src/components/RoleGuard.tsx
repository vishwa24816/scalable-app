'use client';

import React from 'react';
import { useAuth } from '../context/AuthContext';

interface RoleGuardProps {
  children: React.ReactNode;
  allowedRoles: string[];
}

export function RoleGuard({ children, allowedRoles }: RoleGuardProps) {
  const { user, isLoading } = useAuth();

  if (isLoading) return null;

  if (!user || !user.role || !allowedRoles.includes(user.role)) {
    return null;
  }

  return <>{children}</>;
}

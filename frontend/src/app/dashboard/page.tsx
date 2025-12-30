'use client';

import { useAuth } from "@/context/AuthContext";
import { RoleGuard } from "@/components/RoleGuard";

export default function Dashboard() {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <header className="flex justify-between items-center mb-8 bg-white p-4 rounded shadow">
        <h1 className="text-2xl font-bold text-gray-800">Dashboard</h1>
        <div className="flex items-center gap-4">
          <span className="text-gray-600">Welcome, <strong>{user?.name}</strong> ({user?.role})</span>
          <button 
            onClick={logout}
            className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition"
          >
            Logout
          </button>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white p-6 rounded shadow">
          <h2 className="text-xl font-semibold mb-2 text-gray-700">General Info</h2>
          <p className="text-gray-600">Available to all logged-in users.</p>
        </div>

        <RoleGuard allowedRoles={['TEAM_MEMBER', 'SYSTEM_ADMINISTRATOR']}>
          <div className="bg-blue-50 p-6 rounded shadow border border-blue-200">
            <h2 className="text-xl font-semibold mb-2 text-blue-800">Team Actions</h2>
            <p className="text-blue-600">Manage team projects and tasks.</p>
          </div>
        </RoleGuard>

        <RoleGuard allowedRoles={['SYSTEM_ADMINISTRATOR']}>
          <div className="bg-purple-50 p-6 rounded shadow border border-purple-200">
            <h2 className="text-xl font-semibold mb-2 text-purple-800">Admin Panel</h2>
            <p className="text-purple-600">System-wide settings and analytics.</p>
          </div>
        </RoleGuard>
      </div>
    </div>
  );
}

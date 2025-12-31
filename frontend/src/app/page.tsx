'use client';

import { useAuth } from "@/context/AuthContext";
import Link from "next/link";

export default function Home() {
  const { user, isLoading } = useAuth();

  if (isLoading) return <div className="p-8 text-center">Loading...</div>;

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-8 font-[family-name:var(--font-geist-sans)]">
      <main className="max-w-2xl w-full bg-white p-12 rounded-xl shadow-lg flex flex-col gap-8 items-center text-center">
        <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">Foundation & Auth System</h1>
        <p className="text-lg text-gray-600">A scalable web application with authentication and dashboard.</p>
        
        <div className="w-full h-px bg-gray-200"></div>

        {user ? (
          <div className="flex flex-col items-center gap-6">
            <div className="p-4 bg-green-50 text-green-800 rounded-lg border border-green-100 flex items-center gap-2">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
              Logged in as: <strong className="ml-1">{user.email}</strong>
            </div>
            <Link 
              href="/dashboard"
              className="px-8 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition transform hover:scale-105 shadow-md"
            >
              Go to Dashboard
            </Link>
          </div>
        ) : (
          <div className="flex flex-col items-center gap-6 w-full">
            <div className="p-4 bg-yellow-50 text-yellow-800 rounded-lg border border-yellow-100">
              Not logged in. Please sign in to access the dashboard.
            </div>
            <div className="flex gap-4 w-full justify-center">
              <Link 
                href="/login"
                className="flex-1 max-w-[160px] px-6 py-3 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 transition text-center shadow-sm"
              >
                Login
              </Link>
              <Link 
                href="/register"
                className="flex-1 max-w-[160px] px-6 py-3 bg-white text-blue-600 border border-blue-600 rounded-lg font-semibold hover:bg-blue-50 transition text-center shadow-sm"
              >
                Register
              </Link>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

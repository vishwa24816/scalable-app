'use client';

import { useAuth } from "@/context/AuthContext";

export default function Home() {
  const { user, isLoading } = useAuth();

  if (isLoading) return <div className="p-8">Loading...</div>;

  return (
    <div className="p-8 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 items-center sm:items-start">
        <h1 className="text-2xl font-bold">Foundation & Auth System</h1>
        {user ? (
          <div className="p-4 bg-green-100 text-green-800 rounded">
            Logged in as: <strong>{user.email}</strong>
          </div>
        ) : (
          <div className="p-4 bg-yellow-100 text-yellow-800 rounded">
            Not logged in.
          </div>
        )}
      </main>
    </div>
  );
}

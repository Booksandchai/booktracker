
'use client';
import { useState } from 'react';

export default function Home() {
  const [showBuy, setShowBuy] = useState(null);
  const sampleRecs = [
    { id: 'r1', title: 'Spellbound Love', authors: ['C. Nightshade'], thumbnail: 'https://via.placeholder.com/128x192?text=Rec' },
    { id: 'r2', title: 'Enchanted Kingdoms', authors: ['M. Rivers'], thumbnail: 'https://via.placeholder.com/128x192?text=Rec' },
  ];

  return (
    <div className="min-h-screen bg-night text-white font-body flex">
      <aside className="w-64 bg-[#041e13] p-6 flex flex-col gap-8">
        <div className="text-xl font-whimsical flex items-center gap-2">
          <div className="w-8 h-8 bg-gradient-to-br from-green-600 to-green-300 rounded-full flex items-center justify-center">🪄</div>
          <span>SpellShelf</span>
        </div>
        <nav className="flex flex-col gap-4 text-sm">
          <button className="text-left hover:text-brand.light">Dashboard</button>
          <button className="text-left hover:text-brand.light">My Library</button>
        </nav>
      </aside>
      <main className="flex-1 p-10 space-y-10">
        <h1 className="text-3xl font-semibold">Welcome back, Seer</h1>
        <section>
          <h2 className="text-2xl font-medium mb-4">Recommendations</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {sampleRecs.map((r) => (
              <div key={r.id} className="bg-[#0f3d2e] rounded-2xl p-4 flex flex-col justify-between shadow-lg">
                <div className="flex gap-4">
                  <img src={r.thumbnail} alt={r.title} className="w-20 h-28 object-cover rounded-md border border-green-500" />
                  <div className="flex-1">
                    <h3 className="font-semibold">{r.title}</h3>
                    <p className="text-xs text-gray-300">{r.authors.join(', ')}</p>
                  </div>
                </div>
                <div className="mt-4 flex gap-2">
                  <button className="flex-1 bg-gradient-to-r from-green-500 to-green-300 text-black rounded-full px-4 py-2 text-sm font-medium" onClick={() => setShowBuy(r.id)}>Buy locally</button>
                  <button className="border border-green-400 px-4 py-2 rounded-full text-sm">Save</button>
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

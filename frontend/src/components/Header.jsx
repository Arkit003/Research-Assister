import React from 'react';

export default function Header() {
  return (
    <header className="app-header">
      <div className="brand">
        <span className="brand-icon">📑</span>
        <span>Research Assister</span>
      </div>
      <div style={{ fontSize: '14px', color: '#64748b' }}>
        v1.0
      </div>
    </header>
  );
}
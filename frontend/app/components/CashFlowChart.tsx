"use client";

import React from 'react';
import {
  Area,
  CartesianGrid,
  ComposedChart,
  Legend,
  Line,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';

type CashPoint = {
  day: number;
  label: string;
  balance: number;
  forecastLow: number;
  forecastHigh: number;
};

export default function CashFlowChart({ data }: { data: CashPoint[] }) {
  return (
    <div className="h-[500px] w-full rounded-[2rem] border border-[#1A1C20]/10 bg-white p-8 shadow-xl shadow-[#1A1C20]/5 relative overflow-hidden">
      <div className="mb-8 flex items-center justify-between">
        <div>
          <p className="text-xs uppercase tracking-widest text-[#D0B063] font-bold">Predictive Model</p>
          <h2 className="mt-2 text-3xl font-black text-[#1A1C20] font-serif">90-Day Liquidity Forecast</h2>
        </div>
        <span className="rounded-full border border-emerald-500/30 bg-emerald-50 px-4 py-1.5 text-xs font-bold text-emerald-700 shadow-sm">
          High Confidence
        </span>
      </div>

      <ResponsiveContainer width="100%" height="80%">
        <ComposedChart
          data={data}
          margin={{ top: 20, right: 20, left: 10, bottom: 10 }}
        >
          <defs>
            <linearGradient id="goldGradient" x1="0" x2="0" y1="0" y2="1">
              <stop offset="0%" stopColor="#D0B063" stopOpacity={0.4} />
              <stop offset="100%" stopColor="#D0B063" stopOpacity={0.0} />
            </linearGradient>
          </defs>
          <CartesianGrid stroke="#1A1C20" strokeOpacity={0.05} strokeDasharray="3 3" vertical={false} />
          <XAxis dataKey="label" stroke="#1A1C20" strokeOpacity={0.4} tickLine={false} axisLine={false} interval={9} tick={{ fontSize: 12, fontWeight: 500 }} />
          <YAxis stroke="#1A1C20" strokeOpacity={0.4} tickLine={false} axisLine={false} tickFormatter={(value) => `₹${Math.round(value / 1000)}k`} tick={{ fontSize: 12, fontWeight: 500 }} />
          <Tooltip
            formatter={(value: number) => [`₹${value.toLocaleString('en-IN')}`, 'Cash']}
            contentStyle={{ backgroundColor: '#1A1C20', border: 'none', borderRadius: 12, color: '#fff', fontWeight: 'bold' }}
            itemStyle={{ color: '#D0B063' }}
          />
          <Legend wrapperStyle={{ fontWeight: 600, fontSize: 12, color: '#1A1C20' }} />
          <Area type="monotone" dataKey="forecastHigh" stroke="none" fill="url(#goldGradient)" fillOpacity={1} name="Expected Range" />
          <Area type="monotone" dataKey="forecastLow" stroke="none" fill="#D0B063" fillOpacity={0.1} name="Lower Bound" />
          <Line type="monotone" dataKey="balance" stroke="#1A1C20" strokeWidth={4} dot={{ r: 0 }} name="Projected Cash" />
        </ComposedChart>
      </ResponsiveContainer>
    </div>
  );
}

import {
  Activity,
  Bell,
  BrainCircuit,
  CandlestickChart,
  CreditCard,
  Gauge,
  LayoutDashboard,
  LineChart,
  LockKeyhole,
  Radio,
  ShieldCheck,
  SlidersHorizontal,
  Users
} from "lucide-react";
import { MarketChart } from "@/components/market-chart";
import { ThemeToggle } from "@/components/theme-toggle";
import { assets, signals } from "@/lib/market-data";

const navItems = [
  { label: "Dashboard", icon: LayoutDashboard },
  { label: "Live Markets", icon: CandlestickChart },
  { label: "AI Analysis", icon: BrainCircuit },
  { label: "Signals", icon: Radio },
  { label: "Strategies", icon: SlidersHorizontal },
  { label: "Alerts", icon: Bell },
  { label: "Admin", icon: Users }
];

export default function Home() {
  return (
    <main className="min-h-screen terminal-grid bg-slate-100 text-slate-950 transition dark:bg-ink dark:text-slate-50">
      <div className="flex min-h-screen">
        <aside className="hidden w-72 shrink-0 border-r border-line bg-white/78 p-5 shadow-terminal backdrop-blur-xl dark:bg-slate-950/76 lg:block">
          <div className="flex items-center gap-3">
            <div className="grid h-11 w-11 place-items-center rounded bg-ink text-mint dark:bg-white">
              <LineChart size={22} />
            </div>
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-mint">Deriv</p>
              <h1 className="text-xl font-bold">Intelligence</h1>
            </div>
          </div>
          <nav className="mt-10 space-y-2">
            {navItems.map((item, index) => (
              <button
                key={item.label}
                className={`flex w-full items-center gap-3 rounded px-3 py-3 text-left text-sm font-medium transition ${
                  index === 0
                    ? "bg-slate-950 text-white dark:bg-white dark:text-slate-950"
                    : "text-slate-600 hover:bg-slate-200/70 dark:text-slate-300 dark:hover:bg-slate-800"
                }`}
              >
                <item.icon size={18} />
                {item.label}
              </button>
            ))}
          </nav>
          <div className="glass mt-8 rounded p-4">
            <div className="flex items-center gap-2 text-sm font-semibold">
              <ShieldCheck size={18} className="text-mint" />
              Pro Terminal
            </div>
            <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">AI signals, strategy backtests, and live Deriv streaming enabled.</p>
          </div>
        </aside>

        <section className="flex-1 p-4 sm:p-6 xl:p-8">
          <header className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <p className="text-sm font-semibold uppercase tracking-[0.18em] text-mint">Trading Workspace</p>
              <h2 className="mt-1 text-2xl font-bold sm:text-4xl">Deriv Intelligence Terminal</h2>
            </div>
            <div className="flex items-center gap-3">
              <ThemeToggle />
              <button className="flex h-10 items-center gap-2 rounded bg-slate-950 px-4 text-sm font-semibold text-white transition hover:bg-slate-800 dark:bg-white dark:text-slate-950">
                <LockKeyhole size={16} />
                Secure Login
              </button>
            </div>
          </header>

          <div className="mt-6 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
            {assets.map((asset) => (
              <article key={asset.symbol} className="glass rounded p-4">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <p className="text-xs font-semibold text-slate-500 dark:text-slate-400">{asset.symbol}</p>
                    <h3 className="mt-1 text-sm font-semibold">{asset.name}</h3>
                  </div>
                  <span
                    className={`rounded px-2 py-1 text-xs font-bold ${
                      asset.bias === "Bullish"
                        ? "bg-emerald-500/14 text-emerald-500"
                        : asset.bias === "Bearish"
                          ? "bg-rose-500/14 text-rose-500"
                          : "bg-amber-500/14 text-amber-500"
                    }`}
                  >
                    {asset.bias}
                  </span>
                </div>
                <div className="mt-5 flex items-end justify-between">
                  <p className="text-2xl font-bold">{asset.price}</p>
                  <p className={asset.change.startsWith("+") ? "font-semibold text-emerald-500" : "font-semibold text-rose-500"}>{asset.change}</p>
                </div>
                <div className="mt-4 h-2 rounded bg-slate-200 dark:bg-slate-800">
                  <div className="h-2 rounded bg-mint" style={{ width: `${asset.confidence}%` }} />
                </div>
              </article>
            ))}
          </div>

          <div className="mt-6 grid gap-6 xl:grid-cols-[1.6fr_0.9fr]">
            <section className="glass rounded p-4 sm:p-5">
              <div className="flex flex-wrap items-center justify-between gap-3">
                <div>
                  <h3 className="text-lg font-bold">Live Market Analysis</h3>
                  <p className="text-sm text-slate-500 dark:text-slate-400">R_100 price action with EMA overlay and AI trend context.</p>
                </div>
                <div className="flex gap-2">
                  {["1m", "5m", "15m", "1h", "4h"].map((timeframe) => (
                    <button key={timeframe} className="rounded border border-line px-3 py-2 text-xs font-semibold hover:border-mint">
                      {timeframe}
                    </button>
                  ))}
                </div>
              </div>
              <MarketChart />
            </section>

            <section className="glass rounded p-4 sm:p-5">
              <div className="flex items-center gap-2">
                <BrainCircuit className="text-mint" size={20} />
                <h3 className="text-lg font-bold">AI Insight</h3>
              </div>
              <p className="mt-4 text-sm leading-6 text-slate-600 dark:text-slate-300">
                R_100 is showing a bullish continuation setup. EMA slope is positive, RSI is elevated without crossing exhaustion, and recent volatility expansion supports controlled upside.
              </p>
              <div className="mt-5 grid grid-cols-3 gap-3">
                <Metric label="Confidence" value="88%" />
                <Metric label="Risk" value="Medium" />
                <Metric label="Trend" value="Strong" />
              </div>
              <div className="mt-5 rounded border border-line p-4">
                <p className="text-sm font-semibold">Risk Evaluation</p>
                <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">Avoid entries after a 3-candle spike. Preferred entry remains near EMA retest.</p>
              </div>
            </section>
          </div>

          <div className="mt-6 grid gap-6 xl:grid-cols-3">
            <section className="glass rounded p-4 sm:p-5 xl:col-span-2">
              <div className="flex items-center justify-between">
                <h3 className="text-lg font-bold">Signal Center</h3>
                <Activity size={20} className="text-mint" />
              </div>
              <div className="mt-4 overflow-x-auto">
                <table className="w-full min-w-[620px] text-left text-sm">
                  <thead className="text-xs uppercase text-slate-500">
                    <tr>
                      <th className="py-3">Asset</th>
                      <th>Side</th>
                      <th>Entry</th>
                      <th>Target</th>
                      <th>Confidence</th>
                      <th>Risk</th>
                    </tr>
                  </thead>
                  <tbody>
                    {signals.map((signal) => (
                      <tr key={`${signal.asset}-${signal.side}`} className="border-t border-line">
                        <td className="py-4 font-semibold">{signal.asset}</td>
                        <td className={signal.side === "Buy" ? "font-bold text-emerald-500" : "font-bold text-rose-500"}>{signal.side}</td>
                        <td>{signal.entry}</td>
                        <td>{signal.exit}</td>
                        <td>{signal.confidence}%</td>
                        <td>{signal.risk}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </section>

            <section className="glass rounded p-4 sm:p-5">
              <div className="flex items-center gap-2">
                <Gauge size={20} className="text-mint" />
                <h3 className="text-lg font-bold">Strategy Builder</h3>
              </div>
              <div className="mt-4 space-y-3">
                {["EMA 20 crosses EMA 50", "RSI remains below 70", "Volatility above session mean", "AI confidence over 75%"].map((rule) => (
                  <div key={rule} className="rounded border border-line px-3 py-3 text-sm">
                    {rule}
                  </div>
                ))}
              </div>
              <button className="mt-5 w-full rounded bg-mint px-4 py-3 text-sm font-bold text-slate-950">Run Backtest</button>
            </section>
          </div>

          <div className="mt-6 grid gap-6 lg:grid-cols-3">
            <InfoPanel icon={Bell} title="Alerts" body="Price, signal, and indicator alerts with email and push-ready delivery channels." />
            <InfoPanel icon={CreditCard} title="Subscriptions" body="Free, Pro, and Desk plans with feature gating for AI, signals, and backtesting." />
            <InfoPanel icon={Users} title="Admin Monitor" body="User growth, plan revenue, API health, signal outcomes, and worker status." />
          </div>
        </section>
      </div>
    </main>
  );
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded border border-line p-3">
      <p className="text-xs text-slate-500 dark:text-slate-400">{label}</p>
      <p className="mt-1 font-bold">{value}</p>
    </div>
  );
}

function InfoPanel({ icon: Icon, title, body }: { icon: typeof Bell; title: string; body: string }) {
  return (
    <section className="glass rounded p-4">
      <Icon size={20} className="text-mint" />
      <h3 className="mt-3 font-bold">{title}</h3>
      <p className="mt-2 text-sm leading-6 text-slate-500 dark:text-slate-400">{body}</p>
    </section>
  );
}


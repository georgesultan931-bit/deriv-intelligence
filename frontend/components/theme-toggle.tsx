"use client";

import { Moon, Sun } from "lucide-react";
import { useEffect, useState } from "react";

export function ThemeToggle() {
  const [dark, setDark] = useState(true);

  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);

  return (
    <button
      type="button"
      aria-label="Toggle theme"
      onClick={() => setDark((value) => !value)}
      className="grid h-10 w-10 place-items-center rounded border border-line bg-white/70 text-slate-800 shadow-sm transition hover:border-mint dark:bg-slate-900/70 dark:text-slate-100"
    >
      {dark ? <Sun size={18} /> : <Moon size={18} />}
    </button>
  );
}

